from src.chapter4.section_30 import sentences

verbs = list()
for sentence in sentences:
    for word in sentence:
        if word["pos"] == "動詞":
            verbs.append(word["base"])
# 動詞の原型を抜き出す
print(verbs)