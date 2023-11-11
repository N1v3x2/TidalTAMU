import matplotlib.pyplot as plt
#Additional work
#Regular or sports activity
#Do you have a partner
#Mother’s education
#Father’s education
#Mother’s occupation
#Father’s occupation
#Weekly study hours
#Reading non academic material
#Reading Academic material
#Attending seminar
#Impact of projects
#Pct of classes you attend
#Preparation for midterm exams - 2
#Taking notes in classes
#Listening in classes

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance_with_headers.csv')
print(df["Additional work"])
list_one = []
sumOne = 0
list_two = []
sumTwo = 0
for i in range(145):
    if df["Additional work"][i] == 1:
        list_one.append(1)
        sumOne += df["GRADE"][i]
    else:
        list_two.append(2)
        sumTwo += df["GRADE"][i]

data = {'1': (sumOne/len(list_one)), '2': (sumTwo/len(list_two))}


fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(data.keys(), data.values(), color='black',)

plt.xlabel("Yes or No for additional work")
plt.ylabel("Average Grade")
plt.show()