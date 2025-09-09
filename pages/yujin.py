import streamlit as st
import google.generativeai as genai
st.write("🔑 Available secrets:", list(st.secrets.keys()))
# Page title
st.title("💬 Yujin")
st.markdown("👋 Hi, I'm **Yujin** — your personal Mental Health Assistant.")

# Configure Gemini
genai.configure(api_key=st.secrets["gemini_api_key"])
model = genai.GenerativeModel("gemini-2.5-flash")  # fast + cheap

# System instruction (defines Yujin’s personality)
SYSTEM_PROMPT = """
You are Yujin, a warm, empathetic mental health assistant.
- Always reply in a supportive, encouraging tone.
- Give practical and healthy suggestions (like sleep habits, stress relief, journaling, exercise).
- Keep answers short, clear, and positive.
- If asked about serious issues (like self-harm), remind the user to seek professional help.
"""

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm Yujin 🌸 How are you feeling today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
prompt = st.chat_input("Type your message here...")
if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Collect conversation context for Gemini
    convo = [SYSTEM_PROMPT] + [m["content"] for m in st.session_state.messages]

    # Stream bot reply
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_reply = ""

        try:
            for chunk in model.generate_content(convo, stream=True):
                if chunk.text:
                    full_reply += chunk.text
                    placeholder.markdown(full_reply + "▌")
            placeholder.markdown(full_reply)
        except Exception as e:
            full_reply = f"⚠️ Error: {e}"
            placeholder.markdown(full_reply)

    # Save bot reply
    st.session_state.messages.append({"role": "assistant", "content": full_reply})
