# important: setup venv and have pandas and scikit learn installed before running

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression



def predict_final(work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep,
                  notes, listen, prevgpa, course_gpa):
    stuperf_path = "StudentsPerformance_with_headers.csv"
    stuperf_data = pd.read_csv(stuperf_path)
    # print(stuperf_data.columns)
    y = stuperf_data.GRADE
    stuperf_features = ['Additional work', 'Regular artistic or sports activity', 'Do you have a partner',
                        'Weekly study hours', 'Reading frequency',
                        'Reading frequency.1', 'Attendance to the seminars/conferences related to the department',
                        'Impact of your projects/activities on your success',
                        'Attendance to classes', 'Preparation to midterm exams 2', 'Taking notes in classes',
                        'Listening in classes', 'Cumulative grade point average in the last semester (/4.00)', 'COURSE GPA']
    x = stuperf_data[stuperf_features]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    stuperf_model = LogisticRegression()
    stuperf_model.fit(x_train, y_train)

    accuracy = stuperf_model.score(x_test, y_test)
    print("Accuracy:", accuracy)

    data = [[work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa, course_gpa],
            ]
    inpdata = pd.DataFrame(data=data)
    return stuperf_model.predict(inpdata)[0]
