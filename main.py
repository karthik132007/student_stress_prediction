import streamlit as st
import numpy as np
from datetime import datetime
import pickle

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
    st.markdown("---")
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("🔄 Take Assessment Again", type="primary"):
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    
    print(f"Final answers array: {answers}")
    
    # View Result button with radar chart
    if st.button("🎯 View Result Dashboard", type="secondary"):
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
        'text': "Mental Health Assessment Report",
        'x': 0.5,
        'y': 0.9,
        'font': {'size': 20, 'color': 'white', 'family': 'Arial Black'}
    },
    paper_bgcolor='rgba(15, 15, 35, 0.95)',
    plot_bgcolor='rgba(15, 15, 35, 0.95)',
    font=dict(color='white'),
    height=400,   # 🔽 smaller
    margin=dict(t=40, b=40, l=40, r=40)   # 🔽 tighter
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
                           padding: 25px; border-radius: 15px; margin: 10px 0; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
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
                           padding: 25px; border-radius: 15px; margin: 10px 0; box-shadow: 0 8px 32px rgba(0,0,0,0.3);">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
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
            elif prediction_result == "Moderate":
                st.warning("🌤️ Some areas could benefit from attention. Consider focusing on stress management and self-care.")
            elif prediction_result == "At Risk":
                st.error("🚨 Please consider speaking with a mental health professional for personalized support.")
            else:
                st.info("📈 Your assessment has been completed. Focus on the areas with lower scores for improvement.")
                
        except Exception as e:
            st.error(f"❌ Error creating dashboard: {str(e)}")
            st.info("Please make sure plotly is installed: pip install plotly")