from src.chapter4.section_30 import sentences

nouns = list()
for sentence in sentences:
    for word in sentence:
        if word["pos1"] == "サ変接続":
            print(word)
            nouns.append(word["base"])
# サ変接続の名詞を抜き出す
# print(nouns)