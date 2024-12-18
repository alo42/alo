import random
def Vote(chances):
    a = random.randint(0,100)
    if a <= chances:
        return 'Democratic'
    else:
        return 'Republican'

def election(persons, chances):
    str = ''
    d = 0
    r = 0
    for _ in range(persons):
        str = Vote(chances)
        if str == 'Democratic':
            d += 1
        elif str == 'Republican':
            r += 1
    if d > r:
        return 'Democrats win'
    elif d < r:
        return 'Republicans win'
    else:
        election(persons, chances)

def simulation(num, persons, chances):
    a = 0
    b = 0
    str = ''
    for _ in range(num):
        str = election(persons, chances)
        if str == 'Democrats win':
            a += 1
        elif str == 'Republicans win':
            b += 1
    return [a,b]

chances = int(input("Give the chances for the Democtrats: "))

arr = simulation(100, 3000, chances)

print(f"In 100 simulations the Democrats win {arr[0]} times and the Republicans {arr[1]} times")