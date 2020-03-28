import nltk
import re
import nltk
import heapq
import numpy as np


paragraph="""Thank you all so very much. Thank you to the Academy. Thank you to all of you in this room. I have to congratulate the 
other incredible nominees this year. The Revenant was the product of the tireless efforts of an unbelievable cast and crew. First off, 
to my brother in this endeavor, Mr. Tom Hardy. Tom, your talent on screen can only be surpassed by your friendship off screen … thank you 
for creating a transcendent cinematic experience. Thank you to everybody at Fox and New Regency … my entire team. I have to thank everyone 
from the very onset of my career … To my parents; none of this would be possible without you. And to my friends, I love you dearly; you know
 who you are.

And lastly, I just want to say this: Making The Revenant was about man's relationship to the natural world. 
A world that we collectively felt in 2015 as the hottest year in recorded history. Our production needed to move 
to the southern tip of this planet just to be able to find snow. Climate change is real, it is happening right now. It is 
the most urgent threat facing our entire species, and we need to work collectively together and stop procrastinating. We need 
to support leaders around the world who do not speak for the big polluters, but who speak for all of humanity, for the indigenous people 
of the world, for the billions and billions of underprivileged people out there who would be most affected by this. For our children’s 
children, and for those people out there whose voices have been drowned out by the politics of greed. I thank you all for this amazing award
 tonight. Let us not take this planet for granted. I do not take tonight for granted. Thank you so very much. """

sentences = nltk.sent_tokenize(paragraph)


wordCount={}

for i in range(len(sentences)):
    sentences[i]=sentences[i].lower()
    sentences[i]=re.sub(r'\W',' ',sentences[i])
    sentences[i]=re.sub(r'\s+',' ',sentences[i])
    words = nltk.word_tokenize(sentences[i])
    for word in words:
        if word not in wordCount.keys():
            wordCount[word]=1
        else:
            wordCount[word]+=1

frequent_words=heapq.nlargest(100,wordCount,key=wordCount.get)

#IDF
idf={}

for word in frequent_words:
    doc_count=0
    total= len(sentences)
    for sentence in sentences:
        if word in nltk.word_tokenize(sentence):
            doc_count+=1
   
    #print(word,' doc count =',doc_count,' word count=',wordCount[word])
    idf[word]=np.log((total/doc_count)+1)

#print(idf)

#tf

tf={}
for word in frequent_words:
    vc=[]
    for sentence in sentences:
        count=0
        for w in nltk.word_tokenize(sentence):
            if w==word:
                count+=1
        vc.append(count/len(nltk.word_tokenize(sentence)))
    tf[word]=vc

#print(tf)

#tf-idf
tf_idf=[]
for w in tf.keys():
    vc=[]
    for val in tf[w]:
        vc.append(val*idf[w])
    tf_idf.append(vc)

#print(tf_idf)

tfidf_matrix=np.asarray(tf_idf)
tfidf_matrix=np.transpose(tfidf_matrix)

print(tfidf_matrix)