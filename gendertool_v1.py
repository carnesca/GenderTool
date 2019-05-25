import nltk

male_names = nltk.corpus.names.words("male.txt")
fem_names = nltk.corpus.names.words("female.txt")

file = input("Enter the name of your .txt file: ")

open_file = open(file).read()

males = []
females = []

for name in nltk.word_tokenize(open_file):
    if name in male_names:
        males.append(name)
    elif name in fem_names:
        females.append(name)


print(males + females)
print("Your text contained " + str(len(males)) + " male and " + str(len(females)) + " female names.")

perc_male = len(males) / len(nltk.word_tokenize(open_file)) * 100
perc_female = len(females) / len(nltk.word_tokenize(open_file)) * 100

print(str(perc_male)[:4] + "%")
print(str(perc_female)[:4] + "%")