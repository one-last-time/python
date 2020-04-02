# Latent Semantic Analysis 


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

import nltk

# Sample Data
dataset = ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch campaigns to stop pollution and global warming"]

dataset = [line.lower() for line in dataset]

# Creating Tfidf Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)

# Visualizing the Tfidf Model
print(X[0])
print(vectorizer.get_feature_names())

lsa = TruncatedSVD(n_components=4,n_iter=100)
lsa.fit_transform(X)
print(lsa.components_[0])

terms= vectorizer.get_feature_names()
concept_words={}
for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x: x[1],reverse=True)
    sortedTerms=sortedTerms[:10]
    concept_words['concept'+str(i)]=sortedTerms

print(concept_words)

for key in concept_words.keys():
    sentence_score=[]
    for line in dataset:
        score=0
        for word in nltk.word_tokenize(line):
            for concept_key in concept_words[key]:
                if word==concept_key[0]:
                    score+=concept_key[1]
        sentence_score.append(score)
    print(key+':\n')
    for item in sentence_score:
        print(item)

