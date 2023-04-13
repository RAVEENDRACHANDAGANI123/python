import streamlit as st

# Set page title
st.title("BMI Calculator")

# Define input fields
name = st.text_input("Name")
gender = st.radio("Gender", options=["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=120)
address = st.text_input("Address")
hobbies = st.multiselect("Hobbies", options=["Reading", "Running", "Cooking", "Swimming"])
weight = st.number_input("Weight in kg", min_value=0)
height = st.number_input("Height in cm", min_value=0)

# Define BMI calculation function
def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return bmi

# Calculate BMI on button click
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    st.write(f"Your BMI is {bmi:.2f}")
