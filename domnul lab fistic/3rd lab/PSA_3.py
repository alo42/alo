import random

def theater():
    k = 0
    seats = list(range(1, 101))
    persons = list(range(1, 101))

    a = random.choice(seats)
    seats.remove(a)
    persons.remove(1)

    for i in range(2, 100):
        if i in seats:
            persons.remove(i)
            seats.remove(i)
        else:
            a = random.choice(seats)
            persons.remove(i)
            seats.remove(a)

    if 100 in seats:
        k = 1

    return k

def simulation(number):
    k = 0
    for _ in range(number):
        k += theater()
    print("Probability: ", k / number)

simulation(100000)
