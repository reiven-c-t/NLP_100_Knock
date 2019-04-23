from src.chapter4.section_30 import sentences
from collections import Counter

words = list()
for sentence in sentences:
    for word in sentence:
        words.append(word["surface"])

counter = Counter(words)
top_word = counter.most_common()  # 出現頻度降順で並び替え
print(top_word)
