import streamlit as st
st.title("BMI Calculator")
st.set_page_config(page_title="BMI Calculator")

# Create input controls
name = st.text_input("Name:")
gender = st.radio("Gender:", ("Male", "Female", "Other"))
age = st.number_input("Age:", min_value=0, max_value=150, value=25)
address = st.text_input("Address:")
hobbies = st.multiselect("Hobbies:", ["Reading", "Swimming", "Cycling", "Dancing"])
weight = st.number_input("Weight in kg:", min_value=0.0, max_value=500.0, value=70.0, step=0.1)
height = st.number_input("Height in cm:", min_value=0, max_value=300, value=170)

# Calculate BMI and show result
if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.write(f"**BMI:** {bmi:.2f}")

# Show the input values
st.write(f"**Name:** {name}")
st.write(f"**Gender:** {gender}")
st.write(f"**Age:** {age}")
st.write(f"**Address:** {address}")
st.write(f"**Hobbies:** {', '.join(hobbies)}")
st.write(f"**Weight in kg:** {weight}")
st.write(f"**Height in cm:** {height}")
