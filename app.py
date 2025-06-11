import streamlit as st

# App title
st.title("Simple User Info App")

# Inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=150, step=1)

# Button to display output
if st.button("Submit"):
    if name:
      if age <= 18:
        st.warning("You are under 18 years old !")
      elif:
        age < 60:
        st.success(f"Hello, {name}! You are {age} years old. Please proceed !")
      elif age <= 80:
        st.success(f"Hello, {name}! You are {age} years old. Still Young !")
    else:
        st.warning("Please update your KYC details as you have crossed the threshold age of 80")
        
