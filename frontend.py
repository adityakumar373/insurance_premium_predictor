import streamlit as st
import requests

API_URL="http://localhost:8000/predict"

st.title("Insurance Premium Category Predictor")

st.markdown("Enter your details below:")

age=st.number_input("Age", min_value=1, max_value=119, value=30)
weight=st.number_input("Weight (in kg)", min_value=1.0, value=70.0)
height=st.number_input("Height (in cm)", min_value=1.0, value=172.4)
city=st.text_input("City", value="Mumbai")
smoker=st.selectbox("Are you a smoker?", options=[True, False])
income_lpa=st.number_input("Annual Income (in lakhs)", min_value=0.1, value=5.0)
occupation=st.selectbox("Occupation", options=['Accountant', 'Architect', 'Banker', 'Businessman', 'Carpenter', 'Chef', 'Civil Servant', 'Consultant', 'Content Writer', 'Data Analyst', 'Doctor', 'Driver', 'Electrician', 'Engineer', 'Factory Worker', 'Government Employee', 'HR Manager', 'Insurance Agent', 'Lab Technician', 'Lawyer', 'Marketing Manager', 'Nurse', 'Pharmacist', 'Plumber', 'Real Estate Agent', 'Retail Manager', 'Sales Manager', 'Shop Owner', 'Software Engineer', 'Teacher'])

if st.button("Predict Premium Category"):
    user_input={
        "age": age,
        "weight": weight,
        "height": height,
        "city": city,
        "smoker": smoker,
        "income_lpa": income_lpa,
        "occupation": occupation
    }

    try:
        response=requests.post(API_URL, json=user_input)
        if response.status_code==200:
            result=response.json()
            st.success(f"The predicted insurance premium category is: **{result['insurance_premium_category']}**" )
        else:
            st.error(f"API Error: {response.status_code}-{response.text}")    
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Make sure it is running on port 8000")