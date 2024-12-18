import json
from collections import Counter
import matplotlib.pyplot as plt
from datetime import datetime

def get_monthly_frequency(data_list, target_word):
    monthly_counts = Counter()

    for data_item in data_list:
        text = data_item.get("text", "")
        created_at_str = data_item.get("created_at", "")

        if not created_at_str:
            continue

        try:
            timestamp = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S %z")
        except ValueError:
            continue

        words = text.lower().split()
        monthly_counts[timestamp.month] += words.count(target_word.lower())

    return monthly_counts

def draw_bar_chart(monthly_counts):
    months = [1, 2, 3, 10, 11, 12]
    frequencies = [monthly_counts.get(month, 0) for month in months]

    plt.bar(months, frequencies, color='green', alpha=0.7)
    plt.title('Monthly Counts')
    plt.xlabel('Month')
    plt.ylabel('Frequency')
    plt.xticks(months, ['Jan', 'Feb', 'Mar', 'Oct', 'Nov', 'Dec'])

    plt.show()

json_file_name = "C:\\Users\\User\\Desktop\\labsFISHTIC\\3rd lab\\tweets.json"

with open(json_file_name, "r", encoding='utf-8') as json_file:
    data_list = json.load(json_file)

target_word = input("Enter the word to analyze: ")

monthly_counts = get_monthly_frequency(data_list, target_word)

draw_bar_chart(monthly_counts)


