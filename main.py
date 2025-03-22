import streamlit as st
import requests

def get_live_currency_rates():
    api_url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(api_url)
        data = response.json()
        return data.get("rates", {})
    except:
        return {'USD': 1, 'EUR': 0.92, 'PKR': 277.5}  # Fallback values

def convert_units(category, unit_from, unit_to, value, currency_rates):
    conversion_factors = {
        'Length': {'Meter': 1, 'Kilometer': 0.001, 'Centimeter': 100, 'Millimeter': 1000, 'Inch': 39.3701, 'Foot': 3.28084},
        'Weight': {'Kilogram': 1, 'Gram': 1000, 'Pound': 2.20462, 'Ounce': 35.274},
        'Temperature': {'Celsius': lambda x: x, 'Fahrenheit': lambda x: (x * 9/5) + 32},
        'Currency': currency_rates
    }
    
    if category == 'Temperature':
        return conversion_factors[category][unit_to](value)
    else:
        return value * (conversion_factors[category][unit_to] / conversion_factors[category][unit_from])

st.title("Unit Converter")
category = st.selectbox("Select Category", ['Length', 'Weight', 'Temperature', 'Currency'])

currency_rates = get_live_currency_rates()
conversion_factors = {
    'Length': {'Meter': 1, 'Kilometer': 0.001, 'Centimeter': 100, 'Millimeter': 1000, 'Inch': 39.3701, 'Foot': 3.28084},
    'Weight': {'Kilogram': 1, 'Gram': 1000, 'Pound': 2.20462, 'Ounce': 35.274},
    'Temperature': {'Celsius': lambda x: x, 'Fahrenheit': lambda x: (x * 9/5) + 32},
    'Currency': currency_rates
}

if category:
    units = list(conversion_factors[category].keys())
    unit_from = st.selectbox("From Unit", units)
    unit_to = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", value=0.0)
    
    if st.button("Convert"):
        result = convert_units(category, unit_from, unit_to, value, currency_rates)
        st.success(f"Converted Value: {result} {unit_to}")

# Created by © aliabbas
