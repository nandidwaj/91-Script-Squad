from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import re
import csv

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

import re

def extract_info_from_text(text):
    text = text.lower()

    def search_with_variants(variants, pattern_suffix):
        for variant in variants:
            match = re.search(rf"{variant}{pattern_suffix}", text)
            if match:
                return match.group(1).strip()
        return "N/A"

    # Customer Name
    customer_name = search_with_variants(
        variants=["bill to", "to", "customer", "client"],
        pattern_suffix=r"[:\s]*([\w\s,.-]{3,})"
    )

    # Invoice Date
    invoice_date = search_with_variants(
        variants=["invoice date", "date of issue", "issued on", "date"],
        pattern_suffix=r"[:\s]*([0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{2,4})"
    )

    # Invoice Number
    invoice_number = search_with_variants(
        variants=["invoice number", "inv no", "invoice #", "invoice"],
        pattern_suffix=r"[:\s#]*([\w\-]+)"
    )

    # Amount Due
    amount_due = search_with_variants(
        variants=["amount due", "total due", "total", "balance due", "amount payable"],
        pattern_suffix=r"[:\s$]*([\d,]+\.?\d{0,2})"
    )

    return {
        "customer_name": customer_name,
        "invoice_number": invoice_number,
        "invoice_date": invoice_date,
        "amount_due": amount_due
    }
import csv
import os

def save_to_csv(data, file_name="extracted_data.csv"):
    # Check if file exists
    file_exists = os.path.isfile(file_name)

    # Open the file in append mode, or create it if it doesn't exist
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())

        # Write the header only if the file does not exist
        if not file_exists:
            writer.writeheader()

        # Write the extracted data as a new row
        writer.writerow(data)

    print(f"✅ Data appended to {file_name}")

# Example of using the function:
ocr_text = """
© Miced hvoices
Invoice Number | Inv-s397
DEMO - Sliced Invoices Order Number 12345
Suite 54-1204 January 25, 2016
123 Somewhere Street [aE aT oe
Your City AZ 12345
admin@slicedinvoices.com poisiove $93.50
To:
Test Business
123 Somewhere St
Melbourne, VIC 3000
test@test.com
Hrs/aty | Service Rate/Price Adjust Sub Total
Web Design  & al "
1.00 | This is a sample descriptio Eo 0.00% $85.00
Sub Total $85.00
Tax $8.50
Total $93.50
"""

# Assuming extract_info_from_text() is already defined
extracted_data = extract_info_from_text(ocr_text)

# Save extracted data to CSV
save_to_csv(extracted_data)