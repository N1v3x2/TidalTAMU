import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Attendance to classes"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
list_three = []
sumThree = 0
for i in range(145):
    if df["Attendance to classes"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    elif df["Attendance to classes"][i] == 3:
        list_three.append(3)
        sumThree += df["GRADE"][i]
    else:
        list_two.append(2)
        sumTwo += df["GRADE"][i]
lengthOne = len(list_one)
lengthTwo = len(list_two)
lengthThree =len(list_three)
if len(list_one) == 0:
    sumOne = 0
    lengthOne = 1
if len(list_two) == 0:
    sumTwo = 0
    lengthTwo = 1
if len(list_three) == 0:
    sumThree = 0
    lengthThree = 1
data = {'1': (sumOne/lengthOne), '2': (sumTwo/lengthTwo), '3': (sumThree/lengthThree)}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='crimson',)

plt.xlabel("Class Attendance: Always, Sometimes, Never")
plt.ylabel("Average Grade")
plt.show()