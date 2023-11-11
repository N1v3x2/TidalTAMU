from pdfminer.high_level import extract_text
import re

file_path = 'grd20231EN.pdf'

# Extract text using PDFMiner
text_pdfminer = extract_text(file_path)

# Display the first 500 characters of the extracted text for a preview
preview_text_pdfminer = text_pdfminer[:500]

# Regular Expression to match the class data pattern
# This pattern needs to be refined based on the new text structure
class_data_pattern_pdfminer = re.compile(
    r'(AERO-\d+-\d+)\s*'  # Course code pattern, e.g., AERO-201-500
    r'.*?'                # Non-greedy match for any characters until grade percentages
    r'(\d+)\s*%'          # Number of A grades
    r'.*?'                # Non-greedy match for any characters until next grade
    r'(\d+)\s*%'          # Number of B grades
    r'.*?'                # Non-greedy match for any characters until next grade
    r'(\d+)\s*%'          # Number of C grades
    r'.*?'                # Non-greedy match for any characters until next grade
    r'(\d+)\s*%'          # Number of D grades
    r'.*?'                # Non-greedy match for any characters until next grade
    r'(\d+)\s*%',         # Number of F grades
    re.DOTALL             # DOTALL to match across multiple lines
)

# Find all matches in the text
class_data_matches_pdfminer = class_data_pattern_pdfminer.findall(text_pdfminer)

# Preview the first few matches
print(class_data_matches_pdfminer[:5])  # Display first 5 matches for preview



