import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Do you have a partner"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
for i in range(145):
    if df["Do you have a partner"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    else:
        list_two.append(2)
        sumTwo += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': (sumTwo/len(list_two))}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='magenta',)

plt.xlabel("Yes or No Partner")
plt.ylabel("Average Grade")
plt.show()