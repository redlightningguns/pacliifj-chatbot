import os
import streamlit as st
import requests

# Set page title
st.set_page_config(page_title="Legal Research Chat - Gemini 2.5 Pro", page_icon="⚖️")

# App title
st.title("⚖️ Legal Research Chat (Gemini 2.5 Pro Experimental via OpenRouter)")

# Get your OpenRouter API Key from environment variable
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Check if API key exists
if not OPENROUTER_API_KEY:
    st.error("API key not found! Please set OPENROUTER_API_KEY in your app secrets or environment variables.")
else:
    # User input
    user_input = st.text_area("🔎 Ask your legal research question:", height=150)

    if st.button("Ask Gemini 2.5 Pro") and user_input.strip() != "":
        with st.spinner("🤖 Gemini is thinking..."):
            headers = {
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "google/gemini-2.5-pro-exp-03-25",
                "messages": [
                    {"role": "system", "content": "You are a professional legal research assistant. Use clear and simple legal language."},
                    {"role": "user", "content": user_input}
                ],
                "stream": False
            }

            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

                if response.status_code == 200:
                    result = response.json()
                    answer = result["choices"][0]["message"]["content"]
                    st.success(answer)
                else:
                    st.error(f"❌ Failed: {response.status_code} - {response.text}")

            except Exception as e:
                st.error(f"⚠️ Error: {e}")
