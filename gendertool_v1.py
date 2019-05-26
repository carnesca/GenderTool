import nltk
from collections import Counter
import matplotlib.pyplot as plt


male_names = nltk.corpus.names.words("male.txt")
fem_names = nltk.corpus.names.words("female.txt")

#Reads .txt file and tokenizes words
file = input("Enter the name of your .txt file: ")
open_file = open(file).read()

tokenize = nltk.word_tokenize(open_file)

#Takes unique words and puts them into a list
unique_words = []

for name in tokenize:
    if name not in unique_words:
        unique_words.append(name)

#Takes male names and female names out of unique words list created above
males = []
females = []

for name in unique_words:
    if name in male_names:
        males.append(name)
    elif name in fem_names:
        females.append(name)

all_names = males + females

#Caculates percentage of male names and female names
perc_male = len(males) / len(all_names) * 100
perc_female = len(females) / len(all_names) * 100


#Prints pie chart showing % of male vs female names and a whole number of male and female names found in text
labels = ['Male','Female']
sizes = [perc_male,perc_female]
colors = ["#89cff0","#ffb6c1"]
fig1, ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,startangle=90,autopct='%1.0f%%',colors=colors)
ax1.axis('equal') 
plt.show()
print(males + females)
print("Your text contained " + str(len(males)) + " male and " + str(len(females)) + " female names.")