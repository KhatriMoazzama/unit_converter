from multiprocessing import Value
import streamlit as st

st.title("🌎 Unit Converter App")
st.markdown("### Convert Length, Weight and Time Instantly")
st.write("Welcome! select a category, enter a value and get the converted result")

category = st.selectbox("Choose a category",["Length", "Weight", "Time", "Height"])

def convert_units(category, value, unit):
  if category == "Length":
    if unit == "Kilometers to miles":
      return value * 0.621371
    elif unit == "Miles to Kilometers":
      return value / 0.621371
    
  elif category == "Weight":
    if unit == "Kilograms to pounds":
      return value * 2.20462
    elif unit == "Pounds to Kilograms":
      return value / 2.20462
    
  elif category == "Time":
    if unit == "Hours to Minutes":
      return value * 60
    elif unit == "Minutes to Hours": 
      return value / 60
    elif unit == "Hour to Seconds":
      return value * 3600
    elif unit == "Seconds to Hours":
      return value / 3600
    elif unit == "Minutes to seconds":
      return value * 60
    elif unit == "Seconds to Minutes":
      return value / 60
    
  elif category == "Height":
    if unit == " Feets to centimeters":
      return value * 30.48
    elif unit == "centimeters to Feets":
      return value / 30.48

if category == "Length":
  unit = st.selectbox("📏 select a unit", ["Kilometers to miles", "Miles to Kilometers"]) 
elif category == "Weight":
  unit = st.selectbox("⚖ select a unit", ["Pounds to Kilograms", "Kilograms to pounds"]) 
elif category == "Time":
  unit = st.selectbox("🕐 select a unit", ["Seconds to Minutes","Minutes to seconds", "Seconds to Hours","Hour to Seconds", "Minutes to Hours","Hours to Minutes" ]) 
elif category == "Height":
  unit = st.selectbox("📏 select a unit", ["centimeters to Feets"," Feets to centimeters"]) 
value = st.number_input("Enter a value")
if st.button("Convert"):
  result = convert_units(category, value, unit )
  st.success(f"The result is {result:.2f}")
