import streamlit as st
import requests

st.title("🔍 ANPR System")
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    if st.button("Extract Number Plate"):
        with st.spinner("Processing..."):
            files = {'file': (uploaded_file.name, uploaded_file.read(), uploaded_file.type)}
            res = requests.post("http://localhost:8000/extract", files=files)

            if res.status_code == 200:
                result = res.json()
                st.success(f"Detected Number Plate: {result['number_plate']}")
            else:
                st.error("Failed to get response from backend.")
