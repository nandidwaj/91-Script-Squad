from scripts.extract_ocr import extract_text_from_images
from scripts.extract_with_gpt import extract_info_from_text
from scripts.fill_template import fill_template
import os

# Path to your image input folder
image_path = "bills_input"

# Step 1: Extract text from image using OCR (Tesseract)
ocr_output = extract_text_from_images(image_path)

if not ocr_output:
    print("❌ No text found in images.")
    exit()

# Process only the first extracted file
raw_text = list(ocr_output.values())[0]
print("🔍 Raw OCR Text:\n", raw_text)

# Step 2: Process the extracted text with Gen AI model
structured_data = extract_info_from_text(raw_text)
print("\n📦 Extracted Data:\n", structured_data)

# Step 3: Fill the predefined template
if structured_data and isinstance(structured_data, dict) and structured_data != {}:
    filled_template = fill_template(structured_data)
    print("\n🧾 Filled Template:\n", filled_template)
else:
    print("❌ Failed to extract data or data was empty.")
