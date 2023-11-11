import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Reading frequency (NonText)"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
list_three = []
sumThree = 0
for i in range(145):
    if df["Reading frequency (NonText)"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    elif df["Reading frequency (NonText)"][i] == 3:
        list_three.append(3)
        sumThree += df["GRADE"][i]
    else:
        list_two.append(2)
        sumTwo += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': (sumTwo/len(list_two)), '3': (sumThree/len(list_three))}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='silver',)

plt.xlabel("Reading Frequency of Non-Academic Items: None, Sometimes, Often")
plt.ylabel("Average Grade")
plt.show()