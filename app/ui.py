import streamlit as st
import requests

st.title("AI Customer Support Agent")

question = st.text_input("Enter your question: ")

if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            response = requests.post(
                "https://localhost:8000/ask",
                json={"question": question}
            )
        if response.status_code== 200:
            answer = response.json()["answer"]
            st.success(answer)
        else:
            st.error("Error: Unable to get a response from the backend.")
    else:
        st.warning("Please enter a question.")