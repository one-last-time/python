import nltk

text = 'I was born in Bangladesh'
text1='I owe him 50 taka'

words= nltk.word_tokenize(text1)
tag = nltk.pos_tag(words)
nameEnt = nltk.ne_chunk(tag)
nameEnt.draw()