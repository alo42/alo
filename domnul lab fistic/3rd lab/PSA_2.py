
import random
import math

def generate_coordinates_within_circle(radius):
    y = random.uniform(-radius, radius)
    y_limit = math.sqrt(radius**2 - y**2)
    x = random.uniform(-y_limit, y_limit)

    if y >=0:
        return x, y
    else:
        return generate_coordinates_within_circle(radius)

def check_right_half(x, y):
    k = 0
    if x >= 0:
        k = 1
    return k

def check_less(x, y):
    k = 0
    if (x * x + y * y) <= 25:
        k = 1
    return k

def check_more(x, y):
    k = 0
    if (x * x + y * y) >= 25:
        k = 1
    return k

def check_circle(x, y):
    k = 0
    if (x * x + (y-5) * (y-5)) <= 25:
        k = 1
    return k

def simulation(number):
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    for _ in range(number):
        x, y = generate_coordinates_within_circle(10)
        k1 += check_right_half(x, y)
        k2 += check_less(x, y)
        k3 += check_more(x, y)
        k4 += check_circle(x, y)
    print("Probability of landing in the right half of the target:", "{:.2%}".format(k1 / number))
    print("Probability of the dart landing within 5 inches from the center:", "{:.2%}".format(k2 / number))
    print("Probability of the dart landing more than 5 inches from the center:", "{:.2%}".format(k3 / number))
    print("Probability of landing within 5 inches of the point (0, 5):", "{:.2%}".format(k4 / number))


simulation(100000)
