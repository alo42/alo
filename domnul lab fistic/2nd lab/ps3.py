import random

def break_stick(length):
    k = 0
    a = random.uniform(0, length)
    b = length - a
    if a > b:
        c = random.uniform(0, a)
        a = a - c
    else:
        c = random.uniform(0, b)
        b = b - c

    if a + b > c and b + c > a and a + c > b:
        k = 1

    return k

def game(n):
    length = float(input("Give the length of the stick: "))
    k = 0
    for _ in range(n):
        k = k + break_stick(length)
    return k / n


number_simulations = 100000

print("The probability that the 3 piecies can be used to form a triangle is: ", game(number_simulations))