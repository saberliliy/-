from gensim.models import word2vec
import gensim
import logging
import  numpy as np

model = word2vec.Word2Vec.load('word2vec.txt')
c=model["S"].reshape(-1,200)
print(type(c))
print(model["S"])
target_input = np.zeros((1, 1, 200), dtype=np.float32)

print(model.most_similar(positive=c,topn=1))
for r in range(0,200):
    target_input[0,0,r]=c[r]
print(target_input[0,0,])