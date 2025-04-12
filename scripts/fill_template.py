from jinja2 import Template

def fill_template(extracted_data):
    """
    Fills the predefined template with extracted data.
    """
    # Define your template as a string
    template_string = """
    Customer Name: {{ customer_name or 'N/A' }}
    Invoice Number: {{ invoice_number or 'N/A' }}
    Invoice Date: {{ invoice_date or 'N/A' }}
    Amount Due: {{ amount_due or 'N/A' }}
    """

    try:
        # Check if data is in the correct format
        if not isinstance(extracted_data, dict):
            raise ValueError("Expected extracted_data to be a dictionary.")

        # Create and render template
        template = Template(template_string)
        filled_template = template.render(**extracted_data)

        return filled_template
    
    except Exception as e:
        print("❌ Error while filling template:", e)
        return None
