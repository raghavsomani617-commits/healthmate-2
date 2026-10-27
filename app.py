
import streamlit as st

st.set_page_config(
    page_title="HealthMate",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 HealthMate")
st.subheader("Daily Health Checkup Assistant")
st.write("Enter your details below to calculate your BMI.")

name = st.text_input("Your Name")
age = st.number_input("Your Age", min_value=1, max_value=120, value=20)
weight = st.number_input(
    "Weight (kg)", min_value=1.0, max_value=500.0, value=60.0
)
height = st.number_input(
    "Height (cm)", min_value=1.0, max_value=300.0, value=165.0
)

if st.button("Check My BMI"):
    if not name.strip():
        st.error("Please enter your name.")
    else:
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight range"
        elif bmi < 25:
            category = "Healthy-weight range"
        elif bmi < 30:
            category = "Overweight range"
        else:
            category = "Obesity range"

        st.success(f"Hello, {name}!")
        st.metric("Your BMI", f"{bmi:.2f}")
        st.write("**BMI Category:**", category)

        report = (
            f"HealthMate Health Report\n"
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Weight: {weight} kg\n"
            f"Height: {height} cm\n"
            f"BMI: {bmi:.2f}\n"
            f"BMI Category: {category}\n"
            f"Educational screening only, not a diagnosis."
        )

        st.download_button(
            "Download Health Report",
            data=report,
            file_name="HealthMate_Report.txt",
            mime="text/plain"
        )

st.caption("For educational purposes only, not a medical diagnosis.")
