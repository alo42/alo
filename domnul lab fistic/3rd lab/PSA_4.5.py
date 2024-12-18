import json
from collections import Counter
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import string

def remove_punctuation(word):
    word1 = word.strip(string.punctuation)
    return word1

def is_noun(word):
    pos_tags = pos_tag(word_tokenize(word))
    return any(tag.startswith('NN') for _, tag in pos_tags)

def calculate_popularity_rating(freq, norm_retweet, norm_likes):
    return freq * (1.4 + norm_retweet) * (1.2 + norm_likes)

def get_most_popular_nouns(data_list, exclude_words=None, n=10):
    nouns_data = Counter()

    for data_item in data_list:
        text = data_item.get("text", "")
        retweets = data_item.get("retweets", 0)
        likes = data_item.get("likes", 0)

        words = text.lower().split()
        words = [remove_punctuation(word) for word in words]
        nouns = [word for word in words if is_noun(word) and word not in exclude_words]

        for noun in set(nouns):
            nouns_data[noun] += calculate_popularity_rating(1, retweets, likes)

    most_popular_nouns = nouns_data.most_common(n)
    return most_popular_nouns

json_file_name = "C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\tweets.json"

with open(json_file_name, "r", encoding='utf-8') as json_file:
    data_list = json.load(json_file)

exclude_words = ["10%", "90%", "https://t.co/itjfpkoeuy"]

most_popular_nouns = get_most_popular_nouns(data_list, exclude_words)

print("Most popular nouns:")
for noun, rating in most_popular_nouns:
    print(f"{noun}: {rating:.2f}$")
