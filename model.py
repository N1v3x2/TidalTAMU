import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def predict_final(work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep,
                  notes, listen, prevgpa):
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

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=42)
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    stuperf_model = LogisticRegression()
    stuperf_model.fit(x_train, y_train)

    # accuracy = stuperf_model.score(x_test, y_test)
    # print("Accuracy:", accuracy)

    data = [[work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            [work, extracurricular, partner, studyhours, rf1, rf2, seminar, projects, attendance, midtermprep, notes,
             listen, prevgpa],
            ]
    inpdata = pd.DataFrame(data=data)
    return stuperf_model.predict(inpdata)[0] + 1


def correlation_with_grade(variable):
    # alpha of 0.05
    df = pd.read_csv('StudentsPerformance_with_headers.csv')
    contigency = pd.crosstab(df[variable], df['GRADE'])
    chi2, p, dof, expected = stats.chi2_contingency(contigency)
    critical_value = stats.chi2.ppf(0.05, dof)
    if chi2 > critical_value:
        print(f"The test is significance, {variable} and Grades are related")
    else:
        print(
            f"The test is not significance, {variable} and Grades not related")


# correlation_with_grade("Additional work")
# correlation_with_grade("Regular artistic or sports activity")
# correlation_with_grade("Do you have a partner")
# correlation_with_grade("Mothers education")
# correlation_with_grade("Father education ")
# correlation_with_grade("Mothers occupation")
# correlation_with_grade("Father occupation")
# correlation_with_grade("Weekly study hours")
# correlation_with_grade("Reading frequency")
# correlation_with_grade("Reading frequency Academic")
# correlation_with_grade(
#     "Attendance to the seminars/conferences related to the department")
# correlation_with_grade("Impact of your projects/activities on your success")
# correlation_with_grade("Attendance to classes")
# correlation_with_grade("Preparation to midterm exams 2")
# correlation_with_grade("Taking notes in classes")
# correlation_with_grade("Listening in classes")
# correlation_with_grade(
#     "Cumulative grade point average in the last semester (/4.00)")
