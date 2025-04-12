import re

def extract_fields(text):
    data = {}

    patterns = {
        'invoice_number': r'Invoice\s*(Number|No)?[:\-]?\s*(\w+)',
        'customer_name': r'(Customer|Bill To|Billed To)[:\-]?\s*(.+)',
        'invoice_date': r'(Invoice Date|Date)[:\-]?\s*([\d/.\-]+)',
        'amount_due': r'(Amount Due|Total|Total Due)[:\-]?\s*\$?\s*([\d,]+(?:\.\d{2})?)'
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data[key] = match.group(2).strip()

    return data
