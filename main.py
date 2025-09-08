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

        st.header("📋 Questionnaire")
        
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
    
    # View Result button with COMPACT radar chart
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
                # Create COMPACT radar chart - only 6 key metrics
                categories = [
                    'Self Esteem',
                    'Sleep Quality', 
                    'Safety',
                    'Low Anxiety',  # Inverted
                    'Low Depression',  # Inverted
                    'Academic Performance'
                ]
                
                values = [
                    (st.session_state.q1 / 30) * 100,  # Self Esteem
                    (q3_numerical / 5) * 100,  # Sleep Quality
                    (q9_numerical / 5) * 100,  # Safety
                    100 - ((st.session_state.q5 / 20) * 100),  # Low Anxiety (inverted)
                    100 - ((st.session_state.q6 / 30) * 100),  # Low Depression (inverted)
                    (q7_numerical / 5) * 100   # Academic Performance
                ]
                
                # Close the radar chart
                values += values[:1]
                categories += categories[:1]
                
                # Create SMALLER radar chart
                fig = go.Figure()
                
                fig.add_trace(go.Scatterpolar(
                    r=values,
                    theta=categories,
                    fill='toself',
                    fillcolor='rgba(0, 123, 255, 0.2)',
                    line=dict(color='rgb(0, 123, 255)', width=2),
                    marker=dict(size=4),
                    name='Profile'
                ))
                
                fig.update_layout(
                    polar=dict(
                        radialaxis=dict(
                            visible=True,
                            range=[0, 100],
                            showticklabels=False,
                            gridcolor='rgba(128,128,128,0.3)'
                        ),
                        angularaxis=dict(
                            tickfont=dict(size=10)
                        )
                    ),
                    showlegend=False,
                    title=dict(text="Mental Health Profile", x=0.5, font=dict(size=14)),
                    height=250,  # Much smaller!
                    margin=dict(t=30, b=30, l=30, r=30)
                )
                
                # Display compact chart
                st.plotly_chart(fig, use_container_width=True)
            
            # COMPACT status cards in single row
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #007bff, #0056b3); 
                           padding: 15px; border-radius: 10px; text-align: center;">
                    <div style="color: white; font-size: 14px;">Overall Status</div>
                    <div style="color: white; font-size: 20px; font-weight: bold;">{prediction_result}</div>
                </div>
                """, unsafe_allow_html=True)
                
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #ff6b35, #f7931e); 
                           padding: 15px; border-radius: 10px; text-align: center;">
                    <div style="color: white; font-size: 14px;">Anxiety Index</div>
                    <div style="color: white; font-size: 20px; font-weight: bold;">{anxiety_index}</div>
                </div>
                """, unsafe_allow_html=True)
                
            with col3:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #28a745, #20c997); 
                           padding: 15px; border-radius: 10px; text-align: center;">
                    <div style="color: white; font-size: 14px;">Wellbeing Score</div>
                    <div style="color: white; font-size: 20px; font-weight: bold;">{wellbeing_score}</div>
                </div>
                """, unsafe_allow_html=True)
            
            # COMPACT key metrics in 2 columns
            st.markdown("---")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**🧠 Mental Health**")
                st.write(f"• Self Esteem: {st.session_state.q1}/30")
                st.write(f"• Anxiety: {st.session_state.q5}/20")
                st.write(f"• Depression: {st.session_state.q6}/30")
                
            with col2:
                st.markdown("**🏠 Life Quality**")
                st.write(f"• Sleep Quality: {q3_numerical}/5")
                st.write(f"• Safety: {q9_numerical}/5")
                st.write(f"• Basic Needs: {q10_numerical}/5")
            
            # Stylish dark recommendations
            if prediction_result == "Safe":
                st.markdown(f"""
                <div style="background: rgba(0,255,127,0.1); border-left: 4px solid #00ff7f; 
                           padding: 15px; margin: 15px 0; border-radius: 5px;">
                    <span style="color: #00ff7f; font-size: 16px;">🌟</span>
                    <span style="color: white; margin-left: 10px;">Excellent mental health indicators. Keep maintaining your positive habits!</span>
                </div>
                """, unsafe_allow_html=True)
            elif prediction_result == "Moderate":
                st.markdown(f"""
                <div style="background: rgba(255,165,0,0.1); border-left: 4px solid #ffa500; 
                           padding: 15px; margin: 15px 0; border-radius: 5px;">
                    <span style="color: #ffa500; font-size: 16px;">🌤️</span>
                    <span style="color: white; margin-left: 10px;">Some areas could benefit from attention. Focus on stress management.</span>
                </div>
                """, unsafe_allow_html=True)
            elif prediction_result == "At Risk":
                st.markdown(f"""
                <div style="background: rgba(255,75,75,0.1); border-left: 4px solid #ff4b4b; 
                           padding: 15px; margin: 15px 0; border-radius: 5px;">
                    <span style="color: #ff4b4b; font-size: 16px;">🚨</span>
                    <span style="color: white; margin-left: 10px;">Consider speaking with a mental health professional for personalized support.</span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background: rgba(100,149,237,0.1); border-left: 4px solid #6495ed; 
                           padding: 15px; margin: 15px 0; border-radius: 5px;">
                    <span style="color: #6495ed; font-size: 16px;">📈</span>
                    <span style="color: white; margin-left: 10px;">Assessment complete. Focus on areas with lower scores for improvement.</span>
                </div>
                """, unsafe_allow_html=True)
                
        except Exception as e:
            st.error(f"❌ Error creating dashboard: {str(e)}")
            st.info("Please make sure plotly is installed: pip install plotly")