o#!/usr/bin/python3

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize


website="hello guys , listen ! to me with very carefully !! python is a beautiful scripting language , it is used in multiple platform like machine learning , cloud , bigdata......etc ..." 
stop_words = set(stopwords.words('english'))

#tokenize thw words 
word_tokens = word_tokenize(website)
print(word_tokens)

#filtered the sentence means remove the stop words
filtered_sentence = [w for w in word_tokens if not w in stop_words]
print(filtered_sentence)



'''
#second method of filtering the sentence 
filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)
'''
