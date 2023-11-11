from pdfminer.high_level import extract_text
import fitz
import pandas as pd
import collections
import re

file_path = 'grd20231EN.pdf'

# with fitz.open(file_path) as doc:
#     file_text = ''.join([page.get_text() for page in doc])
#     print(file_text)


def read_grade_distributions(path):
    # Extract text using PDFMiner
    text_pdfminer = extract_text(path)

    # Regular Expression to match the class data pattern
    # This pattern needs to be refined based on the new text structure
    class_data_pattern_pdfminer = re.compile(
        r'(\w\w\w\w-\d+)-\d+\s*'    # Course code pattern, e.g., AERO-201-500
        r'.*?'                              # Non-greedy match for any characters until grade percentages
        r'(\d+[.]\d\d)\s*%'                 # Number of A grades
        r'.*?'                              # Non-greedy match for any characters until next grade
        r'(\d+[.]\d\d)\s*%'                 # Number of B grades
        r'.*?'                              # Non-greedy match for any characters until next grade
        r'(\d+[.]\d\d)\s*%'                 # Number of C grades
        r'.*?'                              # Non-greedy match for any characters until next grade
        r'(\d+[.]\d\d)\s*%'                 # Number of D grades
        r'.*?'                              # Non-greedy match for any characters until next grade
        r'(\d+[.]\d\d)\s*%',                # Number of F grades
        re.DOTALL                           # DOTALL to match across multiple lines
    )

    class_dict = collections.defaultdict(list)
    # Find all matches in the text
    for class_data in class_data_pattern_pdfminer.findall(text_pdfminer):
        class_dict[class_data[0]].append(class_data[1:])

    # Preview the first few matches
    for key, val in class_dict.items():
        print(key, val)


# Function to convert grades to numeric values for GPA calculation
def grade_to_points(grade):
    grade_dict = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0, 'TCR': None}
    return grade_dict.get(grade, None)


def read_grade_distributions(path):
    text = extract_text(path)
    print(text)

    # Split the text into lines
    lines = text.split('\n')

    # Initialize an empty list to hold course data
    courses = []

    # Regex patterns for extracting course data
    course_pattern = r'(\w{4})\s+(\d{3})\s+(.+?)\s+(\d+\.\d{3})\s+(\w+|\d+\.\d{3})'
    gpa_pattern = r'GPA:\s+(\d+\.\d{3})'

    # Iterate through lines to extract course data
    for match in re.findall(course_pattern, text):
        subj, num, title, cred, grade = match
        courses.append({'Subject': subj, 'Number': num, 'Title': title, 'Credit': float(cred), 'Grade': grade})

    print(courses)

    # # Convert list of dictionaries to DataFrame
    # df = pd.DataFrame(courses)
    #
    # # Apply function to DataFrame
    # df['Grade Points'] = df['Grade'].apply(grade_to_points)
    #
    # # Calculate GPA for each course
    # df['GPA Contribution'] = df['Grade Points'] * df['Credit']
    #
    # # Group by semester to calculate semester GPAs
    # semester_gpa = df.groupby('Semester')['GPA Contribution', 'Credit'].sum()
    # semester_gpa['GPA'] = semester_gpa['GPA Contribution'] / semester_gpa['Credit']
    #
    # # Calculate cumulative GPA
    # cumulative_gpa = semester_gpa['GPA Contribution'].sum() / semester_gpa['Credit'].sum()
    #
    # # Display results
    # print(semester_gpa)
    # print(f'Cumulative GPA: {cumulative_gpa:.2f}')


read_grade_distributions('transcript.pdf')
