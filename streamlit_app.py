import streamlit as st
import requests

# Hardcoding the OpenRouter API Key (Don't share this key publicly)
OPENROUTER_API_KEY = "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"  # Replace this with your key

# List of available models (you can customize this based on what OpenRouter supports)
available_models = [
    "google/gemini-2.5-pro-exp-03-25",  # Example Gemini model
    "openai/gpt-4",  # Example GPT model
    "openai/gpt-3.5-turbo",  # Another example
]

# Streamlit interface
st.title("Legal Research Chatbot")
st.markdown("Select a model and start chatting!")

# Model selection dropdown
selected_model = st.selectbox("Choose a model", available_models)

# User input for the chat
user_input = st.text_input("Ask a legal question:")

# Function to get response from OpenRouter
def get_response_from_openrouter(model, user_input):
    url = f"https://api.openrouter.ai/v1/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "prompt": user_input,
        "max_tokens": 150,
        "temperature": 0.7,
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    if response.status_code == 200:
        return response_data['choices'][0]['text'].strip()
    else:
        return f"Error: {response_data.get('error', {}).get('message', 'Something went wrong!')}"

# Display the response when the user submits input
if user_input:
    st.write("Thinking...")
    result = get_response_from_openrouter(selected_model, user_input)
    st.write(result)
