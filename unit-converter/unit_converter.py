import streamlit as st

def convert_units(value, unit_from, unit_to):
    
    conversions = {
        "meter_kilomter": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000
    }
    
    key = f"{unit_from}_{unit_to}" # generate a key based on the input and output units
    
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"
    
    st.title("unit Converter")
    
    value = st.number_input("Enter the value")
    
    unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])