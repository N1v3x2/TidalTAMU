import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Regular artistic or sports activity"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
for i in range(145):
    if df["Regular artistic or sports activity"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    else:
        list_two.append(2)
        sumTwo += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': (sumTwo/len(list_two))}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='b',)

plt.xlabel("Yes or No for sports or art activities")
plt.ylabel("Average Grade")
plt.show()