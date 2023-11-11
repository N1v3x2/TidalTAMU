from PyPDF2 import PdfReader
import os

# File path
file_path = 'grd20231EN.pdf'

# Check if the file exists
if os.path.exists(file_path):
    try:
        # Open the PDF file
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)

            # Number of pages in the PDF
            num_pages = len(reader.pages)

            # Extract text from each page
            text = ''
            for page_number in range(num_pages):
                page_obj = reader.pages[page_number]
                text += page_obj.extract_text()

        # Display the first 500 characters of the extracted text for a preview
        preview_text = text[:500]
    except Exception as e:
        preview_text = f"An error occurred: {e}"
else:
    preview_text = "File does not exist."

print(preview_text)

