import json
import nltk
import networkx as nx
import matplotlib.pyplot as plt

import re
import csv
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from itertools import combinations

nltk.download('punkt')
nltk.download('stopwords')

def generate_word_connections(tweets):
    word_connections = {}

    for tweet in tweets:
        text = tweet['text']
        words = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word.isalpha() and word not in stop_words]

        for word1, word2 in combinations(words, 2):
            # Add connections for undirected graph
            word_connections.setdefault(word1, set()).add(word2)
            word_connections.setdefault(word2, set()).add(word1)

    return word_connections

def write_word_connections_to_csv(word_connections, output_csv_path):
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Source', 'Target'])

        for source, targets in word_connections.items():
            for target in targets:
                csv_writer.writerow([source, target])

def visualize_word_connections(csv_file_path):
    G = nx.Graph()

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)  # skip header

        for row in csv_reader:
            source, target = row
            G.add_edge(source, target)

    # Set node sizes based on degree (number of connections)
    node_sizes = [len(list(G.neighbors(node))) * 10 for node in G.nodes]

    # Draw the graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_size=8, node_size=node_sizes, node_color='skyblue', font_color='black')
    plt.show()

def main():
    # Specify the path to tweet.json
    tweet_json_path = 'tweets.json'
    output_csv_path = 'word_connections.csv'

    with open(tweet_json_path, 'r', encoding='utf-8') as file:
        tweets = json.load(file)

    # Select your 200 tweets (modify this part according to your requirements)
    numarul_meu_din_catalog = 23  # replace with your own number
    value = 200 * numarul_meu_din_catalog

    # Extract selected tweets
    selected_tweets = tweets[value:value + 200]

    # Generate word connections
    word_connections = generate_word_connections(selected_tweets)

    # Write word connections to CSV
    write_word_connections_to_csv(word_connections, output_csv_path)
    print(f"Word connections saved to {output_csv_path}")

    # Visualize word connections
    visualize_word_connections(output_csv_path)

if __name__ == "__main__":
    main()
