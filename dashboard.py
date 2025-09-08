import streamlit as st
import requests

st.title("Gemini Chat Integration")

user_input = st.text_input("Ask Gemini something:")

if st.button("Send"):
    if user_input:
        headers = {
            "Authorization": f"Bearer {st.secrets['gemini_api_key']}",
            "Content-Type": "application/json"
        }
        
        data = {
            "prompt": user_input,
            "max_output_tokens": 150  # adjust as needed
        }

        # Replace the URL with the endpoint from Google AI Studio for Gemini
        response = requests.post(
            "https://api.generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generate",
            headers=headers,
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            st.write(result['candidates'][0]['content'])
        else:
            st.error(f"Error {response.status_code}: {response.text}")
