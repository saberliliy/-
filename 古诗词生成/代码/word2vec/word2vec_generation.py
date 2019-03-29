from gensim.models import word2vec
import gensim
import logging

f=open("poetry.txt","r",encoding="utf-8")
text=f.read()
text_cut=" ".join(text).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
        .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '').replace(":","")
fo = open("word_txt.txt", 'w+', encoding='utf-8')
fo.write(text_cut)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus("word_txt.txt")  # 加载语料
model = gensim.models.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5
model.save("word2vec.txt")

print(model["S"])
model.wv.save_word2vec_format("word2vec.txt" + ".bin", binary=True)

