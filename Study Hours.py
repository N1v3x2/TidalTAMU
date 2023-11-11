import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Weekly study hours"])
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
    if df["Weekly study hours"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    elif df["Weekly study hours"][i] == 2:
        list_two.append(2)
        sumTwo += df["GRADE"][i]
    elif df["Weekly study hours"][i] == 3:
        list_three.append(3)
        sumThree += df["GRADE"][i]
    elif df["Weekly study hours"][i] == 4:
        list_four.append(4)
        sumFour += df["GRADE"][i]
    else:
        list_five.append(5)
        sumFive += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': sumTwo/len(list_two), '3': sumThree/len(list_three), '4': sumFour/len(list_four), '5': sumFive/len(list_five)}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='gold',)

plt.xlabel("Hours Studied: None, Under 5 Hours, 6-10 Hours, 11-20 Hours, Over 20 Hours")
plt.ylabel("Average GPA")
plt.show()