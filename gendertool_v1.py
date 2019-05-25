import nltk
from collections import Counter
import matplotlib.pyplot as plt

male_names = nltk.corpus.names.words("male.txt")
fem_names = nltk.corpus.names.words("female.txt")

file = input("Enter the name of your .txt file: ")
open_file = open(file).read()
tokenize_names = nltk.word_tokenize(open_file)

unique_names = []

for name in tokenize_names:
    if name not in unique_names:
        unique_names.append(name)

males = []
females = []

for name in unique_names:
    if name in male_names:
        males.append(name)
    elif name in fem_names:
        females.append(name)


print(males + females)
print("Your text contained " + str(len(males)) + " male and " + str(len(females)) + " female names.")

all_names = males + females

perc_male = len(males) / len(all_names) * 100
perc_female = len(females) / len(all_names) * 100

print("Male: " + str(perc_male)[:2] + "%")
print("Female: " + str(perc_female)[:2] + "%")

# Prints pie chart showing percentage breakdown
labels = ['Male','Female']
sizes = [perc_male,perc_female]
colors = ["#89cff0","#ffb6c1"]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,startangle=90,autopct='%1.0f%%',colors=colors)
ax1.axis('equal') 
plt.show()