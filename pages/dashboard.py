import streamlit as st
import requests
import pandas
# Sidebar navigation
st.sidebar.title("Welcome!")
if st.sidebar.button("📝 Take Self-Assessment"):
    st.switch_page("main.py")
if st.sidebar.button("📊 Dashboard"):
    st.switch_page("dashboard.py")
st.sidebar.empty()
with st.sidebar.expander("Creators :"):
    st.markdown("1. Karthikeya Kumar\n2. Sai Sri Raj\n3. Anand Karthik\n4. Partha Saradhi")
