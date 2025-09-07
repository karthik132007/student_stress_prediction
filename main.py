import streamlit as st
import numpy as np
from datetime import datetime

# Initialize session state
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

st.title("🧠 Mental Health Self-Assessment")

# Start test section
if not st.session_state.test_started:
    if st.button("Start Test"):
        st.session_state.test_started = True
        st.session_state.form_submitted = False
        st.rerun()

# Form section
if st.session_state.test_started and not st.session_state.form_submitted:
    with st.form("mental_health_form"):
        st.header("👤 Personal Info")
        student_name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", min_value=1, max_value=120, value=20)

        st.header("📝 Questionnaire")
        
        st.markdown("<h4 style='font-size:20px;'>1.👉 On a scale of 0 to 30, how confident do you feel about yourself and your abilities?</h4>", unsafe_allow_html=True)
        q1 = st.slider("**Self Esteem**", 0, 30, value=15)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>2.👉 In the past few months, how often have you experienced or felt affected by bullying?</h4>", unsafe_allow_html=True)
        q2_options = [
            "Never",
            "Rarely", 
            "Sometimes",
            "Often",
            "Very Often",
            "Constantly"
        ]
        q2 = st.radio("**Bullying**", q2_options, index=0)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>3.👉 How would you rate your sleep quality recently?</h4>", unsafe_allow_html=True)
        q3_options = [
            "Very Poor",
            "Poor",
            "Below Average", 
            "Average",
            "Good",
            "Excellent"
        ]
        q3 = st.radio("**Sleep Quality**", q3_options, index=3)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>4. 👉 To what extent are you worried about your future career?</h4>", unsafe_allow_html=True)
        q4_options = [
            "Not at all concerned",
            "Slightly concerned",
            "Somewhat concerned",
            "Moderately concerned", 
            "Very concerned",
            "Extremely concerned"
        ]
        q4 = st.radio("**Future Career Concerns**", q4_options, index=2)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>5.👉 On a scale of 0 to 20, how often have you experienced symptoms of anxiety such as nervousness, worry, or restlessness?</h4>", unsafe_allow_html=True)
        q5 = st.slider("**Anxiety Level**", 0, 20, value=5)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>6.👉 On a scale of 0 to 30, how often have you felt down, hopeless, or lost interest in daily activities?</h4>", unsafe_allow_html=True)
        q6 = st.slider("**Depression**", 0, 30, value=5)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>7.👉 How would you rate your academic performance currently?</h4>", unsafe_allow_html=True)
        q7_options = [
            "Very Poor",
            "Poor", 
            "Below Average",
            "Average",
            "Good",
            "Excellent"
        ]
        q7 = st.radio("**Academic Performance**", q7_options, index=3)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>8.👉 How often do you experience headaches?</h4>", unsafe_allow_html=True)
        q8_options = [
            "Never",
            "Rarely",
            "Occasionally", 
            "Sometimes",
            "Often",
            "Very Frequently"
        ]
        q8 = st.radio("**Headache**", q8_options, index=1)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>9.👉 How safe do you feel in your daily environment (home, college, outside)?</h4>", unsafe_allow_html=True)
        q9_options = [
            "Not Safe at All",
            "Rarely Safe",
            "Sometimes Unsafe",
            "Neutral", 
            "Mostly Safe",
            "Very Safe"
        ]
        q9 = st.radio("**Safety**", q9_options, index=4)
        st.markdown("---")
        
        st.markdown("<h4 style='font-size:20px;'>10.👉 To what extent are your basic needs (food, shelter, financial support) being met?</h4>", unsafe_allow_html=True)
        q10_options = [
            "Not Met at All",
            "Rarely Met",
            "Partially Met",
            "Adequately Met",
            "Mostly Met", 
            "Completely Met"
        ]
        q10 = st.radio("**Basic Needs**", q10_options, index=4)

        submitted = st.form_submit_button("Submit Assessment")

        if submitted:
            # Store data in session state
            st.session_state.student_name = student_name
            st.session_state.age = age
            st.session_state.q1 = q1
            st.session_state.q2 = q2
            st.session_state.q2_options = q2_options
            st.session_state.q3 = q3
            st.session_state.q3_options = q3_options
            st.session_state.q4 = q4
            st.session_state.q4_options = q4_options
            st.session_state.q5 = q5
            st.session_state.q6 = q6
            st.session_state.q7 = q7
            st.session_state.q7_options = q7_options
            st.session_state.q8 = q8
            st.session_state.q8_options = q8_options
            st.session_state.q9 = q9
            st.session_state.q9_options = q9_options
            st.session_state.q10 = q10
            st.session_state.q10_options = q10_options
            
            st.session_state.form_submitted = True
            st.rerun()

# Results section
if st.session_state.form_submitted:
    st.success("✅ Assessment Completed Successfully!")
    st.balloons()

    # Convert radio button answers to numerical values (0-5)
    def convert_to_numerical(answer, options_list):
        return options_list.index(answer)

    # Convert all answers to numerical values
    q2_numerical = convert_to_numerical(st.session_state.q2, st.session_state.q2_options)
    q3_numerical = convert_to_numerical(st.session_state.q3, st.session_state.q3_options)
    q4_numerical = convert_to_numerical(st.session_state.q4, st.session_state.q4_options)
    q7_numerical = convert_to_numerical(st.session_state.q7, st.session_state.q7_options)
    q8_numerical = convert_to_numerical(st.session_state.q8, st.session_state.q8_options)
    q9_numerical = convert_to_numerical(st.session_state.q9, st.session_state.q9_options)
    q10_numerical = convert_to_numerical(st.session_state.q10, st.session_state.q10_options)

    # Collect all numerical responses
    answers = np.array([
        st.session_state.q1,  # Already numerical (0-30)
        q2_numerical,  # 0-5
        q3_numerical,  # 0-5
        q4_numerical,  # 0-5
        st.session_state.q5,  # Already numerical (0-20)
        st.session_state.q6,  # Already numerical (0-30)
        q7_numerical,  # 0-5
        q8_numerical,  # 0-5
        q9_numerical,  # 0-5
        q10_numerical  # 0-5
    ])
    
    # Display the numerical answers
    st.subheader("📊 Assessment Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Name:** {st.session_state.student_name}")
        st.write(f"**Age:** {st.session_state.age}")
        st.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    with col2:
        st.write(f"**Numerical Answers Array:**")
        st.code(f"{answers}")
    
    # Display individual scores
    st.subheader("📋 Detailed Scores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**1. Self Esteem:** {st.session_state.q1}/30")
        st.write(f"**2. Bullying:** {q2_numerical}/5 ({st.session_state.q2})")
        st.write(f"**3. Sleep Quality:** {q3_numerical}/5 ({st.session_state.q3})")
        st.write(f"**4. Future Career Concerns:** {q4_numerical}/5 ({st.session_state.q4})")
        st.write(f"**5. Anxiety Level:** {st.session_state.q5}/20")
    
    with col2:
        st.write(f"**6. Depression:** {st.session_state.q6}/30")
        st.write(f"**7. Academic Performance:** {q7_numerical}/5 ({st.session_state.q7})")
        st.write(f"**8. Headache:** {q8_numerical}/5 ({st.session_state.q8})")
        st.write(f"**9. Safety:** {q9_numerical}/5 ({st.session_state.q9})")
        st.write(f"**10. Basic Needs:** {q10_numerical}/5 ({st.session_state.q10})")
    
    # Reset button
    st.markdown("---")
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🔄 Take Assessment Again", type="primary"):
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    print(f"Final answers array: {answers}")