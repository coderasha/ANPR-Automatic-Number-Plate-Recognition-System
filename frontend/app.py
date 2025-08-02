import streamlit as st  
import requests  

st.title("🚗 Indian ANPR System")  
uploaded_file = st.file_uploader("Upload Vehicle Image", type=["jpg", "png"])  

if uploaded_file:  
    files = {"image": uploaded_file}  
    response = requests.post("http://localhost:5000/upload", files=files).json()  
    if "plate" in response:  
        st.success(f"**Detected Plate:** {response['plate']}")  
    else:  
        st.error("No plate found!")  