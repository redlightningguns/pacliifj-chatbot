import streamlit as st
import requests

st.title("Legal Research Chatbot (Ollama)")

user_input = st.text_area("Enter your legal question:")

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://YOUR-OLLAMA-URL-HERE/api/chat",  # Replace this with your Ollama exposed URL
            json={
                "model": "llama3",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=60
        )
        if response.status_code == 200:
            result = response.json()
            return result["message"]["content"]
        else:
            return f"Ollama returned an error: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

if st.button("Ask"):
    if user_input.strip():
        st.write("### AI Response:")
        st.write(ask_ollama(user_input))
    else:
        st.warning("Please type your question.")
