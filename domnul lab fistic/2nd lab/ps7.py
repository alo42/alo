import random

import matplotlib.pyplot as plt


def toss(num):
    k = 0
    for _ in range(num):
        str = random.choice(['head', 'tail'])
        if str == 'head':
            k +=1
    return k

def game(num):
    categories = []
    for number in range(35, 66):
        categories.append(number)
    values = []
    for number in range(35, 66):
        values.append(0)
    for _ in range(num):
        a = toss(100)
        for i in range(len(categories)):
            if a == categories[i]:
                values[i] += 1
    plt.bar(categories, values, color='blue')

    plt.xlabel('Number of Heads in 100 throws')
    plt.ylabel('Values')
    plt.title('Densities distribution:')

    plt.show()

game(10000)
