# This code was created with the help of ChatGPT
# The code takes a PDF file as input, and extracts
# all text annotations and saves them into a csv file.
# The output csv file contains five columns:
# Page Number, Text Content, Author, Creation Date, Modefication Date
# Note that the code depeds on the field names for annotations in
# PDF file.

import fitz  # PyMuPDF
import csv
import os
from datetime import datetime, timedelta
import re

def convert_pdf_date(pdf_date):
    """ Convert the PDF date format (D:YYYYMMDDHHMMSS+TZ or D:YYYYMMDDHHMMSSZ) to a human-readable format. """
    try:
        if pdf_date.startswith("D:"):
            # Remove the "D:" prefix
            pdf_date = pdf_date[2:]

            # Remove single quotes from timezone (e.g., +03'00 -> +0300)
            pdf_date = re.sub(r"'00", "00", pdf_date)

            # Remove the final single quote from the string if it remains after timezone
            pdf_date = pdf_date.replace("'", "")

            # Handle the 'Z' timezone (UTC), remove the 'Z' and treat it as UTC
            if pdf_date.endswith("Z0000"):
                pdf_date = pdf_date[:-5]  # Remove 'Z0000'
                date_obj = datetime.strptime(pdf_date, "%Y%m%d%H%M%S")
                # Convert UTC to +03:00 time zone (add 3 hours)
                date_obj += timedelta(hours=3)
                return date_obj.strftime("%Y-%m-%d %H:%M:%S")  # No timezone offset included

            # Check for timezone format (e.g., +03'00, +0300)
            # Remove the timezone part using regex
            pdf_date = re.sub(r"[+\-]\d{2}00", "", pdf_date)

            # Now parse the date string without the timezone
            date_obj = datetime.strptime(pdf_date, "%Y%m%d%H%M%S")
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")  # Standard format without timezone

        else:
            return "Invalid Date Format"
    
    except Exception:
        return "Invalid Date Format"

def extract_annotations_to_csv(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    annotations = []

    # Loop through the pages in the PDF
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        
        # Loop through the annotations on the page
        for annot in page.annots():
            annot_type = annot.type[1]  # Annotation type name (e.g., "FreeText", "Popup", etc.)

            # Extract the required fields
            annot_text = annot.info.get("content", "")  # Text of the annotation
            author = annot.info.get("title", "Unknown Author")  # Author name
            creation_date = annot.info.get("creationDate", "")
            mod_date = annot.info.get("modDate", "")

            # Convert dates to human-readable format
            creation_date_human = convert_pdf_date(creation_date) if creation_date else "N/A"
            mod_date_human = convert_pdf_date(mod_date) if mod_date else "N/A"

            # If annotation text is found, append to annotations list
            if annot_text:
                annotations.append({
                    "page": page_num + 1,  # 1-indexed
                    "text": annot_text,
                    "author": author,
                    "creation_date": creation_date_human,
                    "mod_date": mod_date_human
                })

    # Generate CSV file name based on the input PDF file name
    output_csv = os.path.splitext(pdf_path)[0] + '.csv'

    # Write annotations to CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Page Number', 'Annotation Text', 'Author', 'Creation Date', 'Modification Date'])  # Write header row

        # Write annotation rows
        for annot in annotations:
            writer.writerow([annot['page'], annot['text'], annot['author'], annot['creation_date'], annot['mod_date']])

    print(f"Annotations have been written to: {output_csv}")


# Main script
if __name__ == "__main__":
    # Ask for the input file path
    input_pdf = input("Enter the full path of the PDF file: ")
    
    # Validate if file exists
    if not os.path.isfile(input_pdf):
        print("The file does not exist. Please check the path and try again.")
    else:
        extract_annotations_to_csv(input_pdf)
