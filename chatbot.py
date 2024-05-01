import streamlit as st
import ollama

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

### Write Message History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

## Generator for Streaming Tokens
def generate_response():
    try:
        response = ollama.chat(model='gemma:2b', stream=True, messages=st.session_state.messages)
        for partial_resp in response:
            token = partial_resp["message"]["content"]
            st.session_state["full_message"] += token
            yield token
    except Exception as e:
        st.error(f"Failed to generate response: {str(e)}")
        return None

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    st.session_state["full_message"] = ""
    response_stream = generate_response()
    if response_stream is not None:
        st.chat_message("assistant", avatar="🤖").write_stream(response_stream)
        st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
    else:
        st.write("Service is currently unavailable, please try again later.")

