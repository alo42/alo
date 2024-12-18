import nltk
from collections import Counter

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')


def get_most_frequent_nouns(text, top_n=10):

    words = nltk.word_tokenize(text)


    pos_tags = nltk.pos_tag(words)


    nouns = [word for word, pos in pos_tags if pos in ('NN', 'NNS')]


    noun_counts = Counter(nouns)


    most_common_nouns = noun_counts.most_common(top_n)

    return most_common_nouns



text = """
In the village, there was a farmer. The farmer had a cow, a horse, and a few chickens. 
Every morning, the farmer would milk the cow and feed the chickens. The horse would run in the field, 
and the village children loved to watch it. The field was vast and full of flowers.
"""


top_nouns = get_most_frequent_nouns(text)
for noun, count in top_nouns:
    print(f"{noun}: {count}")










