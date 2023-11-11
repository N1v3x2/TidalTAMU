import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Listening in classes"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
list_three = []
sumThree = 0
for i in range(145):
    if df["Listening in classes"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    elif df["Listening in classes"][i] == 3:
        list_three.append(3)
        sumThree += df["GRADE"][i]
    else:
        list_two.append(2)
        sumTwo += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': (sumTwo/len(list_two)), '3': (sumThree/len(list_three))}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='orange',)

plt.xlabel("Listen in Class: Never, Sometimes, Always")
plt.ylabel("Average Grade")
plt.show()