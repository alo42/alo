import json
from collections import Counter
import re

def find_words_starting_with_prefix(input_prefix, text):
    input_prefix = input_prefix.lower()

    pattern = r'\b' + re.escape(input_prefix) + r'\w*\b'
    matching_words = re.findall(pattern, text.lower())

    return matching_words

def get_most_frequent_words(words, n=3):
    word_counter = Counter(words)
    most_frequent_words = word_counter.most_common(n)
    return most_frequent_words

json_file_name = "tweets.json"

with open(json_file_name, "r", encoding='utf-8') as json_file:
    data_list = json.load(json_file)

user_input = input("Enter a word to be continued: ")

matching_words = []
for data_item in data_list:
    text = data_item.get("text", "")
    matching_words.extend(find_words_starting_with_prefix(user_input, text))

top_suggestions = get_most_frequent_words(matching_words)

print(f"Suggestions for:  '{user_input}':")
for word, count in top_suggestions:
    print(f"{word} ({count})")

