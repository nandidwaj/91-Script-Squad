# 🧾 AI-Powered Bill Data Extraction

Automated system that extracts key details such as *Customer Name, **Invoice Number, and **Date* from bill/invoice images using *OCR* and *Generative AI, and stores the structured data in an **Excel sheet*.

---

## 🚀 Project Overview

Manual bill entry is tedious and error-prone. This project aims to *automate the process* by combining:
- *OCR (Optical Character Recognition)* to extract raw text from images
- *Generative AI* to intelligently parse and extract structured information
- *Excel generation* to store data in a predefined template

---

## 🎯 Objective

To build a smart solution that reads scanned bills, extracts essential fields, and stores them in a well-organized Excel file — improving accuracy, saving time, and reducing human intervention.

---

## 🧰 Tech Stack
| Category         | Tools / Libraries                                                              |
|------------------|--------------------------------------------------------------------------------|
| OCR Engine       | pytesseract, Pillow (PIL), OpenCV (cv2)                                  |
| Generative AI    | Hugging Face Transformers (transformers), PyTorch (torch)                  |
| Model Used       | google/flan-t5-small                                                         |
| Template Engine  | Jinja2                                                                       |
| Python Utilities | os, pathlib, re, json                                                  |
---

## 🔍 Features

- 📸 Image-to-text extraction using Tesseract OCR  
- 🧠 Intelligent field detection using flan-t5-small  
- 📄 Output organized into structured Excel format  
- 🔁 Supports batch processing of multiple invoices  
- 🧪 Pre-processing with OpenCV for improved OCR accuracy (optional)

---

