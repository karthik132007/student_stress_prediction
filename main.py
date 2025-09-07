import streamlit as st
import numpy as np
from datetime import datetime

# Step 1: Start
st.title("🧠 Mental Health Self-Assessment")
start_test = st.button("Start Test")

if start_test:
    with st.form("mental_health_form"):
        st.header("👤 Personal Info")
        student_name = st.text_input("Enter your name")
        dob = st.date_input("Enter your Date of Birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())

        st.header("📝 Questionnaire")
        self_esteem = st.slider("**1. Self Esteem**", 0, 30)

        bullying = st.radio(
            "**2. Bullying**",
            [
                "Never",
                "Rarely",
                "Sometimes",
                "Often",
                "Very Often",
                "Constantly"
            ]
        )

        sleep_quality = st.radio(
            "**3. Sleep Quality**",
            [
                "Very Poor",
                "Poor",
                "Below Average",
                "Average",
                "Good",
                "Excellent"
            ]
        )

        career_concerns = st.radio(
            "**4. Future Career Concerns**",
            [
                "Not at all concerned",
                "Slightly concerned",
                "Somewhat concerned",
                "Moderately concerned",
                "Very concerned",
                "Extremely concerned"
            ]
        )

        anxiety = st.slider("**5. Anxiety Level**", 0, 21)

        depression = st.slider("**6. Depression**", 0, 27)

        academic = st.radio(
            "**7. Academic Performance**",
            [
                "Very Poor",
                "Poor",
                "Below Average",
                "Average",
                "Good",
                "Excellent"
            ]
        )

        headache = st.radio(
            "**8. Headache**",
            [
                "Never",
                "Rarely",
                "Occasionally",
                "Sometimes",
                "Often",
                "Very Frequently"
            ]
        )

        safety = st.radio(
            "**9. Safety**",
            [
                "Not Safe at All",
                "Rarely Safe",
                "Sometimes Unsafe",
                "Neutral",
                "Mostly Safe",
                "Very Safe"
            ]
        )


        basic_needs = st.radio(
            "**10. Basic Needs**",
            [
                "Not Met at All",
                "Rarely Met",
                "Partially Met",
                "Adequately Met",
                "Mostly Met",
                "Completely Met"
            ]
        )

        submitted = st.form_submit_button("Submit")

    if submitted:
        # Calculate age
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Collect responses
        responses = np.array([
            self_esteem, bullying, sleep_quality, career_concerns,
            anxiety, depression, academic, headache, safety, basic_needs
        ])