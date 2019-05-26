import nltk
import random

#Defines a list of male names and female names
male_names = nltk.corpus.names.words("male.txt")
fem_names = nltk.corpus.names.words("female.txt")

#Reads .txt file here
file = input("Enter the name of your .txt file: ")
open_file = open(file).read()

#Tokenizes words from file
tokenize = nltk.word_tokenize(open_file)

unique_words = []

#Inputs unique words into list
for word in tokenize:
    if word not in unique_words:
        unique_words.append(word)

#Takes names out of unique_words list and puts them into lists for male and female names and all names together
males = []
females = []

for name in unique_words:
    if name in male_names:
        males.append(name)
    elif name in fem_names:
        females.append(name)

all_names = males + females


#Creates test data set for classifier by creating tuble where first entry is dictionary and then randomly shuffles tuple 
def name_feature(name):
    return {"name": name}

names_labeled = ([(name_feature(name), 'male') for name in male_names] + [(name_feature(name), 'female') for name in fem_names])
random.shuffle(names_labeled)

train_set = names_labeled

#Trains classifier based on training set created above 
classifier = nltk.NaiveBayesClassifier.train(train_set)


#Classifies names as male or female
for name in all_names:
    print(name + ": " + str(classifier.classify(name_feature(name))))

print("Your text contained " + str(len(males)) + " male and " + str(len(females)) + " female names.")