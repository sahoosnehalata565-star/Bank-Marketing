# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("my_model.pkl")

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Bank Marketing Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Bank Marketing Prediction App")
st.write("Predict whether a customer will subscribe to a term deposit.")

st.subheader("Enter Customer Details")

# -----------------------------
# Inputs
# -----------------------------

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=None,
    placeholder="Enter age"
)

job = st.selectbox(
    "Job",
    [
        "Select Job",
        'admin.', 'blue-collar', 'entrepreneur', 'housemaid',
        'management', 'retired', 'self-employed', 'services',
        'student', 'technician', 'unemployed', 'unknown'
    ]
)

marital = st.selectbox(
    "Marital Status",
    [
        "Select Marital Status",
        'divorced', 'married', 'single', 'unknown'
    ]
)

education = st.selectbox(
    "Education",
    [
        "Select Education",
        'basic.4y', 'basic.6y', 'basic.9y',
        'high.school', 'illiterate',
        'professional.course', 'university.degree', 'unknown'
    ]
)

default = st.selectbox(
    "Has Credit in Default?",
    ["Select Option", 'no', 'yes', 'unknown']
)

housing = st.selectbox(
    "Housing Loan?",
    ["Select Option", 'no', 'yes', 'unknown']
)

loan = st.selectbox(
    "Personal Loan?",
    ["Select Option", 'no', 'yes', 'unknown']
)

contact = st.selectbox(
    "Contact Type",
    ["Select Contact Type", 'cellular', 'telephone']
)

month = st.selectbox(
    "Last Contact Month",
    [
        "Select Month",
        'jan', 'feb', 'mar', 'apr', 'may', 'jun',
        'jul', 'aug', 'sep', 'oct', 'nov', 'dec'
    ]
)

day_of_week = st.selectbox(
    "Day of Week",
    [
        "Select Day",
        'mon', 'tue', 'wed', 'thu', 'fri'
    ]
)

duration = st.number_input(
    "Call Duration (seconds)",
    min_value=0,
    value=None,
    placeholder="Enter duration"
)

campaign = st.number_input(
    "Number of Contacts During Campaign",
    min_value=1,
    value=None,
    placeholder="Enter campaign contacts"
)

pdays = st.number_input(
    "Days Since Last Contact",
    min_value=0,
    value=None,
    placeholder="Enter pdays"
)

previous = st.number_input(
    "Number of Previous Contacts",
    min_value=0,
    value=None,
    placeholder="Enter previous contacts"
)

poutcome = st.selectbox(
    "Previous Campaign Outcome",
    [
        "Select Outcome",
        'failure', 'nonexistent', 'success'
    ]
)

emp_var_rate = st.number_input(
    "Employment Variation Rate",
    value=None,
    placeholder="Enter employment variation rate"
)

cons_price_idx = st.number_input(
    "Consumer Price Index",
    value=None,
    placeholder="Enter consumer price index"
)

cons_conf_idx = st.number_input(
    "Consumer Confidence Index",
    value=None,
    placeholder="Enter consumer confidence index"
)

euribor3m = st.number_input(
    "Euribor 3 Month Rate",
    value=None,
    placeholder="Enter euribor rate"
)

nr_employed = st.number_input(
    "Number of Employees",
    value=None,
    placeholder="Enter number of employees"
)

# -----------------------------
# Encoding Maps
# -----------------------------

job_map = {
    'admin.': 0,
    'blue-collar': 1,
    'entrepreneur': 2,
    'housemaid': 3,
    'management': 4,
    'retired': 5,
    'self-employed': 6,
    'services': 7,
    'student': 8,
    'technician': 9,
    'unemployed': 10,
    'unknown': 11
}

marital_map = {
    'divorced': 0,
    'married': 1,
    'single': 2,
    'unknown': 3
}

education_map = {
    'basic.4y': 0,
    'basic.6y': 1,
    'basic.9y': 2,
    'high.school': 3,
    'illiterate': 4,
    'professional.course': 5,
    'university.degree': 6,
    'unknown': 7
}

binary_map = {
    'no': 0,
    'yes': 1,
    'unknown': 2
}

contact_map = {
    'cellular': 0,
    'telephone': 1
}

month_map = {
    'jan': 0,
    'feb': 1,
    'mar': 2,
    'apr': 3,
    'may': 4,
    'jun': 5,
    'jul': 6,
    'aug': 7,
    'sep': 8,
    'oct': 9,
    'nov': 10,
    'dec': 11
}

day_map = {
    'mon': 0,
    'tue': 1,
    'wed': 2,
    'thu': 3,
    'fri': 4
}

poutcome_map = {
    'failure': 0,
    'nonexistent': 1,
    'success': 2
}

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

    # Validation
    required_fields = [
        age, duration, campaign, pdays, previous,
        emp_var_rate, cons_price_idx,
        cons_conf_idx, euribor3m, nr_employed
    ]

    dropdown_fields = [
        job, marital, education, default,
        housing, loan, contact,
        month, day_of_week, poutcome
    ]

    if (
        None in required_fields or
        "Select Job" == job or
        "Select Marital Status" == marital or
        "Select Education" == education or
        "Select Option" in [default, housing, loan] or
        "Select Contact Type" == contact or
        "Select Month" == month or
        "Select Day" == day_of_week or
        "Select Outcome" == poutcome
    ):

        st.warning("⚠️ Please fill all fields before prediction.")

    else:

        input_data = pd.DataFrame([{
            'age': age,
            'job': job_map[job],
            'marital': marital_map[marital],
            'education': education_map[education],
            'default': binary_map[default],
            'housing': binary_map[housing],
            'loan': binary_map[loan],
            'contact': contact_map[contact],
            'month': month_map[month],
            'day_of_week': day_map[day_of_week],
            'duration': duration,
            'campaign': campaign,
            'pdays': pdays,
            'previous': previous,
            'poutcome': poutcome_map[poutcome],
            'emp.var.rate': emp_var_rate,
            'cons.price.idx': cons_price_idx,
            'cons.conf.idx': cons_conf_idx,
            'euribor3m': euribor3m,
            'nr.employed': nr_employed
        }])
        
        # Debugging: Show input data and raw prediction output
        st.write("Input Data for Prediction:")
        st.write(input_data)
        
        prediction = model.predict(input_data)
        st.write("Prediction Raw Output:", prediction)  
        if prediction[0] == 1:
            st.success("✅ Customer is likely to subscribe.")
        else:
            st.error("❌ Customer is not likely to subscribe.")