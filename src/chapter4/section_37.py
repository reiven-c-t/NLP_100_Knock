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
top10 = counter.most_common(10)

left = list()
height = list()
label = list()
for idx, item in enumerate(top10):
    left.append(idx)
    label.append(item[0])
    height.append(item[1])

# bar
# https://pythondatascience.plavox.info/matplotlib/棒グラフ
plt.bar(left, height, tick_label=label, align="center")
plt.xlabel("単語")
plt.ylabel("出現個数")
plt.show()
# plt.savefig("/Users/reiven/Documents/Python/NLP_100_Knock/data/chapter4/top10.png")
