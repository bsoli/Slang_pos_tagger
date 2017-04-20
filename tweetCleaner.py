__author__ = 'benso_000'
import nltk
import string
import re
from nltk.corpus import words

def remove_punc(s):
    #removes the punctuation from before and after a word
    return s.strip(string.punctuation)

f = open("slang.txt", 'r')
f2 = open("slangwords.txt", 'w')
tweets = f.read().split()
slang_words = []
words = words.words()
pattern = re.compile(r'.*[0-9]|RT|.*http|.*#|.*@') #regular expression to elimate numbers, links, hashtags, and names
for word in tweets:
    if remove_punc(word) not in words and not (pattern.match(word)) and remove_punc(word) not in slang_words:
            word = remove_punc(word)  #loops through each words to determine if the word is slang then writes the word to a file
            slang_words.append(word)
            f2.write(word+'\n')



        

