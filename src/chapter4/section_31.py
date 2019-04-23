from src.chapter4.section_30 import sentences

verbs = list()
for sentence in sentences:
    for word in sentence:
        if word["pos"] == "動詞":
            verbs.append(word["surface"])

# 動詞を抜き出す
print(verbs)
