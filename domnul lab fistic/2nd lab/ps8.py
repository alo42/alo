import random

def table(persons):
    arr = list(range(persons))
    random.shuffle(arr)
    lunch = arr.copy()
    random.shuffle(arr)
    dinner = arr.copy()

    if lunch[0] != dinner[0] and lunch[-1] != dinner[-1]:
        for j in range(persons - 1):
            for i in range(persons - 1):
                if (lunch[j] == dinner[i] and lunch[j+1] == dinner[i+1]) or \
                   (lunch[j] == dinner[i+1] and lunch[j+1] == dinner[i]):
                    return 0
    else:
        return 0

    return 1

def simulation(num, n):
    k = 0
    for _ in range(num):
        k += table(n)
    return k / num

persons = int(input("Give the number of persons: "))

p = simulation(100000, persons)

print(f"The probability that two persons will not sit next to each other for {persons} persons is: {p}")

