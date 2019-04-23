import codecs
from os import path
from collections import OrderedDict  # 見やすさのためのOrderedDict

data_folder_path = "/Users/reiven/Documents/Python/NLP_100_Knock/data/chapter4"
parsed_data_path = path.join(data_folder_path, "neko.txt.mecab")

with codecs.open(parsed_data_path, "r", "utf-8") as f:
    mecab_data = f.readlines()
    parsed_data = list()  # MeCabの単純なpython listへの変換データ(Not 課題案件)
    for line in mecab_data:
        column = OrderedDict()
        # 1行の順序: http://d.hatena.ne.jp/Kshi_Kshi/20110102/1293920002
        column["surface"] = line.split()[0]
        try:
            other_column_data = line.split()[1].split(",")
        except IndexError:
            print("EOL!")
            # print(line.split())

        try:
            column["base"] = other_column_data[6]
            column["pos"] = other_column_data[0]
            column["pos1"] = other_column_data[1]
            parsed_data.append(column)
        except IndexError:
            pass
            # print("space")
            # print(other_column_data)

    sentences = list()
    sentence = list()
    for morpheme in parsed_data:
        sentence.append(morpheme)
        if morpheme["pos1"] == "句点":
            sentences.append(sentence)
            sentence = list()

# sentenceのlistに[{surface: 出現形, pos: 品詞, pos1:品詞情報1}, ...]の形式で1文の構成単語の形態素情報が入っている
# sentencesのlistに[sentence, ...]の形で情報が入っている
