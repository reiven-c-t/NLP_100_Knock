from src.chapter4.section_30 import sentences

sequences = list()
for sentence in sentences:
    for idx, word in enumerate(sentence):
        if word["surface"] == "の" and sentence[idx - 1]["pos"] == sentence[idx + 1]["pos"] == "名詞":
            sequence = (sentence[idx - 1], word, sentence[idx + 1])
            sequences.append(sequence)

# 名詞A の 名詞B 的な単語列を検知しsequence setに突っ込んで, sequenceをsequencesに突っ込む
# print(nouns)
