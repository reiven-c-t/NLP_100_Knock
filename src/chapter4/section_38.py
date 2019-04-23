from src.chapter4.section_30 import sentences
from collections import Counter
import matplotlib.pyplot as plt
# 日本語フォント問題
# https://qiita.com/yniji/items/3fac25c2ffa316990d0c
import matplotlib as mpl
font = {"family": "AppleGothic"}
mpl.rc('font', **font)


words = list()
for sentence in sentences:
    for word in sentence:
        words.append(word["surface"])

counter = Counter(words)
word_count = counter.most_common()

data = list()
height = list()
label = list()
for idx, item in enumerate(word_count):
    data.append(item[1])

# bar
# https://pythondatascience.plavox.info/matplotlib/棒グラフ
plt.hist(data, bins=20, range=(1, 20))
plt.xlabel("単語出現頻度")
plt.show()
# plt.savefig("/Users/reiven/Documents/Python/NLP_100_Knock/data/chapter4/word_hist.png")
