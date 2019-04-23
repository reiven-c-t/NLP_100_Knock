from src.chapter4.section_30 import sentences
from collections import Counter

words = list()
for sentence in sentences:
    for word in sentence:
        words.append(word["surface"])

counter = Counter(words)
word_count = counter.most_common()

import matplotlib.pyplot as plt

# 日本語フォント問題
# https://qiita.com/yniji/items/3fac25c2ffa316990d0c
import matplotlib as mpl

font = {"family": "AppleGothic"}
mpl.rc('font', **font)

left = list()
height = list()
label = list()
from math import log

for idx, item in enumerate(word_count):
    log_x = log(idx + 1)
    log_y = log(item[1])
    left.append(log_x)
    # label.append(item[0])
    height.append(log_y)

# bar
# https://pythondatascience.plavox.info/matplotlib/棒グラフ

plt.plot(left, height)
plt.ylabel("単語出現頻度")
plt.xlabel("単語出現頻度順位(降順)")
plt.show()
# plt.savefig("/Users/reiven/Documents/Python/NLP_100_Knock/data/chapter4/log-log.png")
