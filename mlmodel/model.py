#important: setup venv and have pandas and scikit learn installed before running

import pandas as pd
from sklearn.tree import DecisionTreeRegressor


#test data by init dataframe

def predict_final(work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes, listen, prevgpa):
    stuperf_path = "StudentsPerformance_with_headers.csv"
    stuperf_data = pd.read_csv(stuperf_path)
    # print(stuperf_data.columns)
    y = stuperf_data.GRADE
    stuperf_features = ['Additional work', 'Regular artistic or sports activity', 'Do you have a partner',
                        'Weekly study hours', 'Reading frequency',
                        'Reading frequency.1', 'Attendance to the seminars/conferences related to the department',
                        'Impact of your projects/activities on your success',
                        'Attendance to classes', 'Preparation to midterm exams 2', 'Taking notes in classes',
                        'Listening in classes', 'Cumulative grade point average in the last semester (/4.00)']

    x = stuperf_data[stuperf_features]
    # print(x.describe())
    # print(x.head())

    stuperf_model = DecisionTreeRegressor(random_state=1)
    stuperf_model.fit(x, y)
    data = {
        'Additional work': [work], 'Regular artistic or sports activity': [extracurricular], 'Do you have a partner': [partner],
        'Weekly study hours': [studyhours], 'Reading frequency': [rf1],
        'Reading frequency.1': [rf2], 'Attendance to the seminars/conferences related to the department': [seminar],
        'Impact of your projects/activities on your success': [projects],
        'Attendance to classes': [attendance], 'Preparation to midterm exams 2': [midtermprep], 'Taking notes in classes': [notes],
        'Listening in classes': [listen], 'Cumulative grade point average in the last semester (/4.00)': [prevgpa]
    }
    # print("predicting gpa for head data:")
    # print(inpdata)
    # print("calculated final grade is:")
    # print(stuperf_model.predict(inpdata))
    inpdata = pd.DataFrame(data=data)
    return (stuperf_model.predict(inpdata)[0]+2)


