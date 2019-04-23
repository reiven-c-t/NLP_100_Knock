import MeCab
import codecs
from os import path

data_folder_path = "/Users/reiven/Documents/Python/NLP_100_Knock/data/chapter4"
raw_data_path = path.join(data_folder_path, "neko.txt")
parsed_data_path = path.join(data_folder_path, "neko.txt.mecab")

mecab = MeCab.Tagger()

with codecs.open(raw_data_path, "r", "utf-8") as f:
    text = f.read()

parsed = mecab.parse(text)  # どうせデータがメモリに乗るのでparseでよい

with codecs.open(parsed_data_path, "w", "utf-8") as f:
    f.write(parsed)
