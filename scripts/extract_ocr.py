import pytesseract
import os

# Set Tesseract path if not in system PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Extract text from image using Tesseract OCR (without preprocessing)
def extract_text_from_image(image_path):
    """
    Extract text from the given image using Tesseract OCR without preprocessing.
    """
    try:
        # Use config to boost OCR for blocks of text
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(image_path, config=custom_config)
        return text.strip()
    except Exception as e:
        print(f"❌ Failed to extract text from {image_path}: {e}")
        return None

# Main function to process all images in the directory
def extract_text_from_images(input_dir):
    """
    Extract text from all images in the given directory using Tesseract OCR.
    """
    extracted_texts = {}

    if not os.path.exists(input_dir):
        print(f"❌ Input directory '{input_dir}' does not exist.")
        return extracted_texts

    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(input_dir, file_name)
            try:
                # Extract text directly from the image
                text = extract_text_from_image(image_path)
                if text:
                    extracted_texts[os.path.splitext(file_name)[0]] = text
            except Exception as e:
                print(f"❌ Failed to process {file_name}: {e}")

    return extracted_texts


# Example Usage
if __name__ == "__main__":
    input_directory = "path_to_your_image_directory"
    extracted_texts = extract_text_from_images(input_directory)

    # Print the extracted texts
    for file_name, text in extracted_texts.items():
        print(f"Extracted Text from {file_name}:\n{text}\n")
