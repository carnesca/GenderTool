import nltk

male_names = nltk.corpus.names.words("male.txt")
fem_names = nltk.corpus.names.words("female.txt")

name = input("Enter the name here: ")

if name in male_names:
    print("This is a male name.")
elif name in fem_names:
    print("This is a female name.")
else:
    print("This name was not found in the database.")