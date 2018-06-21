#!/usr/bin/python3

from nltk.corpus import wordnet

key_word=input("enter keyword")

#printing wordnet function

print(wordnet.synsets(key_word))

new_dict=[]
#print examples
print(new_dict[0].examples())

#print definition
print(new_dict[0].definition())