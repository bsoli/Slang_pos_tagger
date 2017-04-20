import re

def tag(s):
    #takes  a word and matches the word to a patten
    #if no pattern matches, the word is assumed to be a noun
    for i in range(len(patterns)-1):
        pattern = re.compile(patterns[i])
        if re.match(pattern, s.lower()):
            return '('+s+', '+pos[i]+')'
    return '('+s+', '+'NN'+')'
f = open('slangwords.txt', 'r')
f2 = open('taggedslang.txt', 'w')
slang = f.read().split()
# a list of regular expression morphological patterns
patterns = [
    r'.*ing$|.*in$',  
    r'.*ed$', 
    r'.*es$',
    r'.*n\'t$|.*\'ve|.*[aioI][nm][nm]a$',
    r'.*esque$|^ir.|^un.|.*less$|.*ous$|.*ful$', 
    r'.*\'s$',
    r'.*sss',
    r'.*s$', 
    r'.*\'ll$|\'d',  
    r'.*ly$' 
    ]   
# a list of POS tags whose indices correspond to regEx patterns
pos = [
    "VBG",  #Gerund
    "VBD",  #Past Tense verb
    "VBZ",  #Present tense verb
    "VB",   #Verb
    "ADJ",  #Adjective
    "NN$",  #Possesive
    "INT",  #Interjection
    "NNS",  #Plural noun
    "MOD",  #Modal
    "ADV"  #Adverb
    ]

for word in slang:
    f2.write(tag(word)+'\n')


