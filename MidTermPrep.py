import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Preparation to midterm exams 2"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
list_three = []
sumThree = 0
for i in range(145):
    if df["Preparation to midterm exams 2"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    elif df["Preparation to midterm exams 2"][i] == 3:
        list_three.append(3)
        sumThree += df["GRADE"][i]
    else:
        list_two.append(2)
        sumTwo += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': (sumTwo/len(list_two)), '3': (sumThree/len(list_three))}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='deepskyblue',)

plt.xlabel("Time Spent Midterm Prep: Close to Exam, All Semester, Never")
plt.ylabel("Average Grade")
plt.show()