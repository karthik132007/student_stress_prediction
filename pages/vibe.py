# vibe.py
import streamlit as st

def mood_recommender():


    if mood == "Happy":
        st.video("https://www.youtube.com/watch?v=ZbZSe6N_BXs")  # Happy - Pharrell Williams
    elif mood == "Sad":
        st.video("https://www.youtube.com/watch?v=RB-RcX5DS5A")  # Fix You - Coldplay
    elif mood == "Stressed":
        st.video("https://www.youtube.com/watch?v=2OEL4P1Rz04")  # Relaxing piano
    elif mood == "Relaxed":
        st.video("https://www.youtube.com/watch?v=1ZYbU82GVz4")  # Chill lofi hip hop
    elif mood == "Motivated":
        st.video("https://www.youtube.com/watch?v=mgmVOuLgFB0")  # Eye of the Tiger
    elif mood == "Angry":
        st.video("https://www.youtube.com/watch?v=hTWKbfoikeg")  # Nirvana - Smells Like Teen Spirit

    return mood

st.subheader("🎵 How are you feeling right now?")
mood = st.radio(
        "Select your current mood:",
        ["Happy", "Sad", "Stressed", "Relaxed", "Motivated", "Angry"]
    )