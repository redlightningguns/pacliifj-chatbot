import streamlit as st
import requests

st.title("Legal Research Chatbot (OpenRouter.ai)")

user_input = st.text_area("Enter your legal question:")

OPENROUTER_API_KEY = "YOUR-OPENROUTER-KEY-HERE"  # Replace with your API Key

def ask_openrouter(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mistral/mistral-7b-instruct",  # You can change the model if you prefer
            "messages": [{"role": "user", "content": prompt}],
        }
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=60)
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            return f"OpenRouter returned error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Error: {e}"

if st.button("Ask"):
    if user_input.strip():
        st.write("### AI Response:")
        st.write(ask_openrouter(user_input))
    else:
        st.warning("Please type your question.")
