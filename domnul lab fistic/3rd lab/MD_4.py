import json
import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')



def extract_hashtags(text):
    
    return re.findall(r'#\w+', text)


def load_emotion_dictionary(file_path):
    emotion_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word, score = line.strip().split('\t')
            emotion_dict[word] = int(score)
    return emotion_dict

def compute_emotional_value(text, emotion_dict):
    # Tokenize the tweet text
    words = word_tokenize(text.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Compute emotional value for each word
    emotional_value = sum(emotion_dict.get(word, 0) for word in words)

    return emotional_value



emotion_dictionary_path = 'AFINN-111.txt'
tweet_json_path = 'tweets.json'
output_file_path = 'emotion_results.txt'
emotion_dict = load_emotion_dictionary(emotion_dictionary_path)
with open(tweet_json_path, 'r', encoding='utf-8') as file:
    tweets = json.load(file)

hashtag_counter = Counter()
for tweet in tweets:
    hashtags = extract_hashtags(tweet['text'])
    hashtag_counter.update(hashtags)

print("Top 10 Hashtags:")
for hashtag, count in hashtag_counter.most_common(10):
    print(f"{hashtag}: {count} occurrences")

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for tweet in tweets:
        tweet_id = tweet['id']
        tweet_text = tweet['text']
        emotional_value = compute_emotional_value(tweet_text, emotion_dict)
        output_file.write(f"{tweet_id}\t{emotional_value}\n")
print("Emotional values computed and stored in emotion_results.txt")
sorted_tweets = sorted(tweets, key=lambda x: compute_emotional_value(x['text'], emotion_dict))
print("\nTop 10 Most Positive Tweets:")
for tweet in sorted_tweets[-10:]:
    print(f"{tweet['id']}: {compute_emotional_value(tweet['text'], emotion_dict)} - {tweet['text']}")
print("\nTop 10 Most Negative Tweets:")
for tweet in sorted_tweets[:10]:
    print(f"{tweet['id']}: {compute_emotional_value(tweet['text'], emotion_dict)} - {tweet['text']}")

