import streamlit as st

def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000
    }
    
    key = f"{unit_from}_{unit_to}"  # Generate a key based on the input and output units
    
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported"

# Streamlit App
st.title("Unit Converter")

# Input Value
value = st.number_input("Enter the value", min_value=0.0, step=0.1)

# Unit Selection
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# Convert Button
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")
