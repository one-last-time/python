import nltk
from nltk.corpus import wordnet

s=input('enter a negtive sentence : ')
#I am not happy
s=s.lower()

tmp=''
words=[]
for w in nltk.word_tokenize(s):
    word=w
    if tmp=='not':
        antonyms=[]
        for syn in wordnet.synsets(word):
            for s in syn.lemmas():
                for a in s.antonyms():
                    antonyms.append(a.name())
                    #print(a.name())
        if len(antonyms)>0:
            word=antonyms[0]
            
        else:
            word=tmp+'_'+w
        tmp=''
    if w=='not':
        tmp=w
    if w!='not':
        words.append(word)

s=' '.join(words)
print(s)
        
