from src.chapter4.section_30 import sentences

sequences = list()
for sentence in sentences:
    idx = 0
    while idx < len(sentence):
        if sentence[idx]["pos"] == "名詞":
            sequence = list()
            sequence.append(sentence[idx])
            while idx < len(sentence):
                idx += 1
                if sentence[idx]["pos"] == "名詞":
                    sequence.append(sentence[idx])
                else:
                    sequences.append(sequence)
                    break
        idx += 1

# 全ての文章を1分ずつ次の検査にかける
# 文先頭のwordが名詞であるかを判別
# wordを初めて検知した場合空のsequence listを生成
# wordを検知した場合sequenceにwordを投入
# wordを検知しsequenceに投入したあと,次のwordが名詞であるかどうかを判別(上に戻る)
# wordを検知しなかった場合sequenceをsequencesに投入しsequenceを再生成し2個上に戻る
# 全ての文章を上記手続きで検査し生成したものがsequencesである

for sequence in sequences:
    word = ""
    for morp in sequence:
        word += morp["surface"]
    print(word)
