import json
from collections import Counter

def get_suggestions(input_word, data_list, suggestions_count=3):
    input_word = input_word.lower()
    suggestions_data = Counter()

    for data_item in data_list:
        text = data_item.get("text", "")
        words = text.lower().split()

        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]

            if current_word == input_word:
                suggestions_data[next_word] += 1

    top_suggestions = suggestions_data.most_common(suggestions_count)

    print(f"Suggestions for '{input_word}':")
    for suggestion, count in top_suggestions:
        print(f"{suggestion} ({count})")

json_file_name = "tweets.json"

with open(json_file_name, "r", encoding='utf-8') as json_file:
    data_list = json.load(json_file)

user_input = input("Enter a word: ")

get_suggestions(user_input, data_list)
