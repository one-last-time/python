import random
import nltk

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

random.seed(38)
n=2

ngram={}

words= nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram=' '.join(words[i:i+n])
    if gram not in ngram.keys():
        ngram[gram]=[]
    ngram[gram].append(words[i+n])

currengram= ' '.join(words[0:n])

result=currengram

for i in range(30):
    if currengram not in ngram.keys():
        break
    
    choices=ngram[currengram]
    result+=' '+choices[random.randrange(len(choices))]
    rword=nltk.word_tokenize(result)
    currengram=' '.join(rword[len(rword)-n:len(rword)])

print(result)

