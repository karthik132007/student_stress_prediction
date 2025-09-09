import streamlit as st
import numpy as np
from datetime import datetime
import pickle
import streamlit.components.v1 as components
import gspread
from google.oauth2.service_account import Credentials
import uuid
import pandas as pd
from fpdf import FPDF
import streamlit as st

st.toast("Use the arrow on the top-left corner to open the sidebar menu!")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SHEET_ID = "1BLltyU70nZ4gxCesSp7RrkhBrgW_UUMTSqNdaNcpnUc"

from pathlib import Path

def get_gs_client():
    if "gcp_service_account" in st.secrets:
        creds = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"], scopes=SCOPES
        )
    else:
        creds = Credentials.from_service_account_file(
            "pivotal-leaf-471506-p3-651eda94f85e.json", scopes=SCOPES
        )
    return gspread.authorize(creds)

if "phone_num" not in st.session_state:
    st.session_state.phone_num = ""
if "student_name" not in st.session_state:
    st.session_state.student_name = ""
if "age" not in st.session_state:
    st.session_state.age = ""
st.sidebar.title("Welcome!")
st.sidebar.empty()
with st.sidebar.expander("Creators :"):
    st.markdown("1. Karthikeya Kumar\n2. Sai Sri Raj\n3. Anand Karthik\n4. Partha Saradhi")
    
# Initialize session state
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

st.title("🧠 Mental Health Self-Assessment")
st.markdown("---")
col1,col2=st.columns(2,gap="large")
with col1:
    st.image("people-with-mental-health-vector.jpg",use_container_width =True)
with col2:
    st.subheader("What Is This App?")
    st.text("Mental health is crucial for living a balanced and happy life. This app helps you track your mood, stress, and self-esteem, visualize trends over time, and gain insights to improve your overall well-being")
# Start test section
st.text("\n")
st.text("\n")
st.text("\n")
phone_num=st.text_input("Enter Your Phone Number")
if not st.session_state.test_started:
    _, center, _ = st.columns((2, 1, 2))
    if center.button("Start Test"):
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
            st.session_state.phone_num=phone_num
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
    
    # Display basic info
    st.subheader("📊 Assessment Results")
    st.write(f"**Name:** {st.session_state.student_name}")
    st.write(f"**Age:** {st.session_state.age}")
    st.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")

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
    # st.markdown("---")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("🔄 Take Assessment Again", type="secondary"):
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    with col2:
        view=st.button("🎯 View Result", type="primary")
    # View Result button with radar chart
    if view:
        import time
        progress = st.progress(0)

        for percent in range(100):
            time.sleep(0.05)
            progress.progress(percent + 1)

        st.success("Done! ✅")
        try:
            # Try to import plotly
            try:
                import plotly.graph_objects as go
                plotly_available = True
            except ImportError:
                plotly_available = False
                st.warning("⚠️ Plotly not installed. Install it with: pip install plotly")
            
            # Get ML prediction
            prediction_result = "Assessment Complete"
            prediction_color = "#00ff7f"
            
            try:
                with open("model.pkl", "rb") as f:
                    model = pickle.load(f)
                
                # Simple normalization for prediction
                mu = np.mean(answers)
                std = np.std(answers) if np.std(answers) != 0 else 1
                ans_normal = (answers - mu) / std
                
                x_input = np.array(ans_normal).reshape(1, -1)
                preds = model.predict(x_input)
                pred_value = int(preds[0]) if isinstance(preds, np.ndarray) else int(preds)
                
                if pred_value == 0:
                    prediction_result = "Safe"
                    prediction_color = "#00ff7f"
                elif pred_value == 1:
                    prediction_result = "Moderate"
                    prediction_color = "#ffa500"
                else:
                    prediction_result = "At Risk"
                    prediction_color = "#ff4444"
                    
            except Exception as e:
                st.info(f"ℹ️ Model prediction unavailable: {str(e)}")
            
            # Calculate metrics
            anxiety_index = st.session_state.q5 + st.session_state.q6 + q4_numerical
            resilience_score = st.session_state.q1 + q3_numerical + q9_numerical + q10_numerical
            wellbeing_score = (st.session_state.q1 + q3_numerical + q9_numerical + q10_numerical) - \
                             (st.session_state.q5 + st.session_state.q6 + q2_numerical + q4_numerical)
            
            if plotly_available:
                # Create radar chart data - normalize all to 0-40 scale for better visualization
                categories = [
                    'Self Esteem',
                    'Sleep Quality', 
                    'Safety',
                    'Basic Needs',
                    'Academic Performance',
                    'Low Anxiety',  # Inverted
                    'Low Depression',  # Inverted
                    'Anti-Bullying',  # Inverted
                    'Career Confidence',  # Inverted
                    'Headache Free'  # Inverted
                ]
                
                values = [
                    (st.session_state.q1 / 30) * 40,  # Self Esteem (0-30 to 0-40)
                    (q3_numerical / 5) * 40,  # Sleep Quality (0-5 to 0-40)
                    (q9_numerical / 5) * 40,  # Safety (0-5 to 0-40)
                    (q10_numerical / 5) * 40,  # Basic Needs (0-5 to 0-40)
                    (q7_numerical / 5) * 40,  # Academic Performance (0-5 to 0-40)
                    40 - ((st.session_state.q5 / 20) * 40),  # Low Anxiety (inverted)
                    40 - ((st.session_state.q6 / 30) * 40),  # Low Depression (inverted)
                    40 - ((q2_numerical / 5) * 40),  # Anti-Bullying (inverted)
                    40 - ((q4_numerical / 5) * 40),  # Career Confidence (inverted)
                    40 - ((q8_numerical / 5) * 40)   # Headache Free (inverted)
                ]
                
                # Close the radar chart
                values += values[:1]
                categories += categories[:1]
                try:
                    client = get_gs_client()
                    sh = client.open_by_key(SHEET_ID).sheet1

                    timestamp = datetime.utcnow().isoformat()

                    row = [
                    st.session_state.phone_num,
                    st.session_state.student_name,
                    st.session_state.age,
                    timestamp,
                    st.session_state.q1,
                    q2_numerical,
                    q3_numerical,
                    q4_numerical,
                    st.session_state.q5,
                    st.session_state.q6,
                    q7_numerical,
                    q8_numerical,
                    q9_numerical,
                    q10_numerical,
                    int(pred_value),
                    anxiety_index,
                    resilience_score,
                    wellbeing_score
                    ]
                    sh.append_row(row)
                    st.success("Saved response to Google Sheets ✅")
                except Exception as e:
                    st.error(f"Failed to save to Google Sheets: {e}")
                
                # Create the radar chart
                fig = go.Figure()
                
                fig.add_trace(go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself',
                    fillcolor='rgba(0, 255, 127, 0.25)',
                    line=dict(color='rgb(0, 255, 127)', width=3),
                    marker=dict(size=8, color='rgb(0, 255, 127)', 
                               line=dict(width=2, color='white')),
                    name='Mental Health Profile'
                ))
                
                fig.update_layout(
    polar=dict(
        bgcolor='rgba(15, 15, 35, 0.95)',
        radialaxis=dict(
            visible=True,
            range=[0, 40],
            showticklabels=True,
            tickfont=dict(color='rgba(255,255,255,0.8)', size=9),
            gridcolor='rgba(255,255,255,0.2)',
            linecolor='rgba(255,255,255,0.3)',
            tick0=0,
            dtick=10
        ),
        angularaxis=dict(
            tickfont=dict(color='white', size=10, family='Arial'),
            linecolor='rgba(255,255,255,0.3)',
            gridcolor='rgba(255,255,255,0.2)'
        )
    ),
    showlegend=False,
    title={
        'text': "",
        'x': 0.5,
        'y': 0.9,
        'font': {'size': 20, 'color': 'white', 'family': 'Arial Black'}
    },
    paper_bgcolor='rgba(15, 15, 35, 0.95)',
    plot_bgcolor='rgba(15, 15, 35, 0.95)',
    font=dict(color='white'),
    height=400,   # 🔽 smaller
    margin=dict(t=50, b=50, l=90, r=90)   # 🔽 tighter
)

                # Display the chart with smaller size
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.plotly_chart(fig, use_container_width=True)
            
            # Create stylized metric cards
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); 
                           padding: 5px; border-radius: 15px; margin: 10px 0; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <span style="color: {prediction_color}; font-size: 24px; margin-right: 15px;">💚</span>
                        <span style="color: white; font-size: 18px; font-weight: bold;">Overall Status</span>
                    </div>
                    <div style="color: white; font-size: 36px; font-weight: bold; margin: 10px 0; text-align: center;">
                        {prediction_result}
                    </div>
                    <div style="color: rgba(255,255,255,0.7); font-size: 14px; text-align: center;">
                        Mental Health Assessment
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #fc4a1a 0%, #f7b733 100%); 
                           padding: 5px; border-radius: 15px; margin: 10px 0; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <span style="color: white; font-size: 24px; margin-right: 15px;">⚡</span>
                        <span style="color: white; font-size: 18px; font-weight: bold;">Anxiety Index</span>
                    </div>
                    <div style="color: white; font-size: 36px; font-weight: bold; margin: 10px 0; text-align: center;">
                        {anxiety_index}
                    </div>
                    <div style="color: rgba(255,255,255,0.7); font-size: 14px; text-align: center;">
                        Combined Stress Level
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Key metrics breakdown
            st.markdown("---")
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); 
                       padding: 25px; border-radius: 15px; margin: 20px 0; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
                <h3 style="color: white; margin-bottom: 25px; text-align: center; font-size: 24px;">
                    📊 Key Metrics Breakdown
                </h3>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; 
                                   padding: 15px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <span style="color: rgba(255,255,255,0.9); font-size: 16px;">Resilience Score</span>
                            <span style="color: #00ff7f; font-size: 22px; font-weight: bold;">{resilience_score}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; 
                                   padding: 15px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <span style="color: rgba(255,255,255,0.9); font-size: 16px;">Self Esteem</span>
                            <span style="color: #00ff7f; font-size: 22px; font-weight: bold;">{st.session_state.q1}/30</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; 
                                   padding: 15px 0;">
                            <span style="color: rgba(255,255,255,0.9); font-size: 16px;">Sleep Quality</span>
                            <span style="color: #00ff7f; font-size: 22px; font-weight: bold;">{q3_numerical}/5</span>
                        </div>
                    </div>
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; 
                                   padding: 15px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <span style="color: rgba(255,255,255,0.9); font-size: 16px;">Wellbeing Score</span>
                            <span style="color: #f7b733; font-size: 22px; font-weight: bold;">{wellbeing_score}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; 
                                   padding: 15px 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
                            <span style="color: rgba(255,255,255,0.9); font-size: 16px;">Safety Level</span>
                            <span style="color: #00ff7f; font-size: 22px; font-weight: bold;">{q9_numerical}/5</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; 
                                   padding: 15px 0;">
                            <span style="color: rgba(255,255,255,0.9); font-size: 16px;">Basic Needs</span>
                            <span style="color: #00ff7f; font-size: 22px; font-weight: bold;">{q10_numerical}/5</span>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Add recommendations based on results
            st.markdown("### 💡 Recommendations")
            
            if prediction_result == "Safe":
                st.success("🌟 Great job! Your mental health indicators are positive. Keep maintaining your healthy habits!")
                st.success("🍃 Keep nurturing your routine—it’s working!")
            elif prediction_result == "Moderate":
                st.warning("🌤️ Some areas could benefit from attention. Consider focusing on stress management and self-care.")
                st.warning("🍵 Limit caffeine and stay hydrated")
            elif prediction_result == "At Risk":
                st.error("🚨 Please consider speaking with a mental health professional for personalized support.")
                st.error("🧘 Try mindfulness or meditation daily.")
            else:
                st.info("📈 Your assessment has been completed. Focus on the areas with lower scores for improvement.")
                
        except Exception as e:
            st.error(f"❌ Error creating dashboard: {str(e)}")
            st.info("Please make sure plotly is installed: pip install plotly")
        def generate_pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Title
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(200, 10, txt="Mental Health Self-Assessment Report", ln=True, align="C")
            pdf.ln(10)

    # Basic Info
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt=f"Name: {st.session_state.student_name}", ln=True)
            pdf.cell(200, 10, txt=f"Age: {st.session_state.age}", ln=True)
            pdf.cell(200, 10, txt=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
            pdf.ln(10)

    # Scores
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, txt="Detailed Scores:", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, 
            f"1. Self Esteem: {st.session_state.q1}/30\n"
            f"2. Bullying: {st.session_state.q2}\n"
            f"3. Sleep Quality: {st.session_state.q3}\n"
            f"4. Future Career Concerns: {st.session_state.q4}\n"
            f"5. Anxiety Level: {st.session_state.q5}/20\n"
            f"6. Depression: {st.session_state.q6}/30\n"
            f"7. Academic Performance: {st.session_state.q7}\n"
            f"8. Headache: {st.session_state.q8}\n"
            f"9. Safety: {st.session_state.q9}\n"
            f"10. Basic Needs: {st.session_state.q10}\n"
            f"10. Basic Needs: {st.session_state.q10}\n"
            )
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, txt="Results:", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, 
            f"1. Stress Level: {prediction_result}/30\n"
            f"2. anxiety index: {anxiety_index}\n"
            f"3. Resilience Score: {resilience_score}\n"
            f"4. Wellbeing Score: {wellbeing_score}\n"
            )
            

            return pdf.output(dest="S").encode("latin-1")
        st.markdown("\n")

        pdf_data = generate_pdf()
        st.download_button(
            label="📄 Download Report as PDF",
            data=pdf_data,
            file_name="assessment_report.pdf",
            mime="application/pdf",type="primary"
)
        # help line 
        st.markdown("---")
        st.subheader("Top Mental Health Care Centers In India")
        df=pd.read_csv("top_10_mental_health_hospitals_india.csv")
        st.dataframe(df, height=200, width=700) 
        st.markdown("---")
        # chat bot
        # Configure Gemini with API key from secrets
        
    st.markdown("---")    
    st.subheader("Faq's")   
    with st.expander("How to open My Dashbrard?"):
        st.markdown("Click on arrow icon on top left corner and navigate to it")
    with st.expander("Why are you asking my phone number?"):
        st.markdown("To identify 'unique' user and save your data to make dashboard")
    with st.expander("Is my data safe?"):
        st.markdown("Your data will be stored in private Database to make 'personalized' dashboard for you")
    