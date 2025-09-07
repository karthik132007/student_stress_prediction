import streamlit as st
import numpy as np
from datetime import datetime

# Step 1: Start
st.title("🧠 Mental Health Self-Assessment")
start_test = st.button("Start Test")
answers=[]
if start_test:
    with st.form("mental_health_form"):
        st.header("👤 Personal Info")
        student_name = st.text_input("Enter your name")
        age = st.number_input("Enter your age",)

        st.header("📝 Questionnaire")
        
        st.markdown("<h4 style='font-size:20px;'>1.👉 On a scale of 0 to 30, how confident do you feel about yourself and your abilities?</h4>", unsafe_allow_html=True)
        q1 = st.slider("**Self Esteem**", 0, 30)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>2.👉 In the past few months, how often have you experienced or felt affected by bullying?</h4>", unsafe_allow_html=True)
        q2 = st.radio(
            "**Bullying**",
            [
                "Never",
                "Rarely",
                "Sometimes",
                "Often",
                "Very Often",
                "Constantly"
            ]
        )
        st.markdown("---")
        st.markdown("<h4 style='font-size:20px;'>3.👉 How would you rate your sleep quality recently?</h4>", unsafe_allow_html=True)
        q3 = st.radio(
            "**Sleep Quality**",
            [
                "Very Poor",
                "Poor",
                "Below Average",
                "Average",
                "Good",
                "Excellent"
            ]
        )
        st.markdown("---")
        st.markdown("<h4 style='font-size:20px;'>4. 👉 To what extent are you worried about your future career?</h4>", unsafe_allow_html=True)
        q4 = st.radio(
            "**Future Career Concerns**",
            [
                "Not at all concerned",
                "Slightly concerned",
                "Somewhat concerned",
                "Moderately concerned",
                "Very concerned",
                "Extremely concerned"
            ]
        )
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>5 .👉 On a scale of 0 to 20, how often have you experienced symptoms of anxiety such as nervousness, worry, or restlessness?</h4>", unsafe_allow_html=True)
        q5= st.slider("**Anxiety Level**", 0, 20)
        st.markdown("---")
        st.markdown("<h4 style='font-size:20px;'>6.👉 On a scale of 0 to 30, how often have you felt down, hopeless, or lost interest in daily activities?</h4>", unsafe_allow_html=True)
        q6 = st.slider("**6. Depression**", 0, 30)
        st.markdown("---")
        

        st.markdown("<h4 style='font-size:20px;'>7.👉 How would you rate your academic performance currently?</h4>", unsafe_allow_html=True)
        q7 = st.radio(
            "**Academic Performance**",
            [
                "Very Poor",
                "Poor",
                "Below Average",
                "Average",
                "Good",
                "Excellent"
            ]
        )
        st.markdown("---")
        st.markdown("<h4 style='font-size:20px;'>8.👉 How often do you experience headaches?</h4>", unsafe_allow_html=True)
        q8 = st.radio(
            "**Headache**",
            [
                "Never",
                "Rarely",
                "Occasionally",
                "Sometimes",
                "Often",
                "Very Frequently"
            ]
        )
        st.markdown("---")
        st.markdown("<h4 style='font-size:20px;'>9.👉 How safe do you feel in your daily environment (home, college, outside)?</h4>", unsafe_allow_html=True)
        q9 = st.radio(
            "**Safety**",
            [
                "Not Safe at All",
                "Rarely Safe",
                "Sometimes Unsafe",
                "Neutral",
                "Mostly Safe",
                "Very Safe"
            ]
        )
        st.markdown("---")
        st.markdown("<h4 style='font-size:20px;'>10.👉 To what extent are your basic needs (food, shelter, financial support) being met?</h4>", unsafe_allow_html=True)
        q10 = st.radio(
            "**Basic Needs**",
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
        st.success("Submitted Successfully")
        st.balloons()

        # Collect responses
        answers = np.array([
            q1,q2,q3,q4,q5,q6,q7,q8,q9,q10
        ])
        
print(answers)