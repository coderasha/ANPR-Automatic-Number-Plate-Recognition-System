import streamlit as st
from utils.detect_plate import detect_and_crop_plate
from utils.enhance_image import enhance_plate_image
from utils.ocr_reader import recognize_plate_text
import os

st.set_page_config(page_title="ANPR India", layout="centered")
st.title("Indian ANPR Platform 🇮🇳")
st.markdown("Upload a vehicle image to detect and read the number plate.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    file_path = f"sample_images/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:
        cropped_path = detect_and_crop_plate(file_path)
        enhanced_path = enhance_plate_image(cropped_path)
        plate_text = recognize_plate_text(enhanced_path)

        st.image(enhanced_path, caption="Enhanced Number Plate", use_column_width=True)
        st.success(f"**Detected Number Plate:** `{plate_text}`")

    except Exception as e:
        st.error(f"Error: {str(e)}")
