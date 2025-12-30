import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload"

st.title("Mobile File Upload")

username = st.text_input("Username")
file = st.file_uploader("Choose a file")

if st.button("Upload"):
    if username and file:
        response = requests.post(
            API_URL,
            params={"username": username},
            files={"file": (file.name, file.getvalue())}
        )
        st.write(response.json())
    else:
        st.warning("Please provide username and file")
