import json
from collections import Counter
import string

def get_most_common_words(text, n=10):
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()
    words = text.split()
    word_counter = Counter(words)
    most_common_words = word_counter.most_common(n)
    return most_common_words


json_file_name = "C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\tweets.json"
with open("C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\tweets.json", "r", encoding="utf-8") as json_file:
    data_list = json.load(json_file)

all_texts = ' '.join([data_item.get("text", "") for data_item in data_list])

most_common_words_all = get_most_common_words(all_texts, n=10)

print("\nMost frequent words:")
for word, count in most_common_words_all:
    print(f"{word}  => {count}")
