import streamlit as st
import os
import csv
from PIL import Image
from scripts.extract_ocr import extract_text_from_images
from scripts.extract_with_gpt import extract_info_from_text
from scripts.fill_template import fill_template

# Create the upload directory
UPLOAD_FOLDER = "bills_input"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="Invoice Extractor", layout="centered")
st.title("🧾 Invoice Extractor")

# File uploader
uploaded_file = st.file_uploader("Upload an Invoice Image", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully!")

    # Perform OCR
    with st.spinner("🔍 Extracting text from invoice..."):
        ocr_output = extract_text_from_images(UPLOAD_FOLDER)
        raw_text = list(ocr_output.values())[0]
        extracted_data = extract_info_from_text(raw_text)
        filled_template = fill_template(extracted_data)

    # Display Extracted Info
    st.subheader("📦 Extracted Data")
    for key, value in extracted_data.items():
        st.markdown(f"**{key.replace('_', ' ').title()}**: {value}")

    # Display filled template
    st.subheader("🧾 Filled Template")
    st.code(filled_template, language="text")

    # Save to CSV
    csv_path = "extracted_data.csv"
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=extracted_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(extracted_data)

    # ✅ Delete the uploaded file after extraction
    try:
        os.remove(file_path)
        st.info(f"Temporary file '{uploaded_file.name}' deleted after processing.")
    except Exception as e:
        st.warning(f"Failed to delete temporary file: {e}")

    st.success("Data saved to CSV.")
