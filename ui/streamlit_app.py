import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/api"

st.title("🔥 RoastBot 3000 🔥")

# Login section
st.subheader("Login")
token = st.text_input("Enter Firebase ID Token", type="password")
if st.button("Login"):
    response = requests.post(f"{API_URL}/login", json={"id_token": token})
    st.json(response.json())

# Roast section
st.subheader("Get Roasted!")
message = st.text_input("Enter your message")
if st.button("Roast Me!"):
    response = requests.post(f"{API_URL}/roast", json={"message": message})
    st.json(response.json())
