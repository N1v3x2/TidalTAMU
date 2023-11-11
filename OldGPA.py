import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Cumulative grade point average in the last semester (/4.00)"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
list_three = []
sumThree = 0
list_four = []
sumFour = 0
list_five = []
sumFive = 0
list_six = []
sumSix = 0
for i in range(145):
    if df["Cumulative grade point average in the last semester (/4.00)"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    elif df["Cumulative grade point average in the last semester (/4.00)"][i] == 2:
        list_two.append(2)
        sumTwo += df["GRADE"][i]
    elif df["Cumulative grade point average in the last semester (/4.00)"][i] == 3:
        list_three.append(3)
        sumThree += df["GRADE"][i]
    elif df["Cumulative grade point average in the last semester (/4.00)"][i] == 4:
        list_four.append(4)
        sumFour += df["GRADE"][i]
    else:
        list_five.append(5)
        sumFive += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': sumTwo/len(list_two), '3': sumThree/len(list_three), '4': sumFour/len(list_four), '5': sumFive/len(list_five)}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='maroon',)

plt.xlabel("GPA Last Semester: < 2.0, 2.00-2.49, 2.50-2.99, 3.00-3.49, >= 3.5")
plt.ylabel("Average GPA")
plt.show()