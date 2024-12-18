import json
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from collections import Counter
import string

def is_noun_starting_with_capital(word):
    if word.istitle():
        pos_tags = pos_tag(word_tokenize(word))
        return any(tag.startswith('NN') for _, tag in pos_tags)

def get_most_common_nouns(text, n=10):
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    words = text.split()
    nouns = [word for word in words if is_noun_starting_with_capital(word)]
    noun_counter = Counter(nouns)
    most_common_nouns = noun_counter.most_common(n)
    return most_common_nouns

json_file_name = "C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\tweets.json"

with open( "C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\tweets.json", "r", encoding='utf-8') as json_file:
    data_list = json.load(json_file)

all_texts = ' '.join([data_item.get("text", "") for data_item in data_list])

most_common_nouns_all = get_most_common_nouns(all_texts)

print("\nMost frequent nouns with capital letter:")
for noun, count in most_common_nouns_all:
    print(f"{noun} {count}")

