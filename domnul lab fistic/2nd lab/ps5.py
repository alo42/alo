import random

def birth():
    a = random.choice([0, 1])  
    if a == 0:
        return 'boy'
    elif a == 1:
        return 'girl'
    else:
        return 'eu'

def simulate_until_boy(num):
    c = 0
    for _ in range(num):  
        k = 1
        child = birth()
        while child != 'boy':
            k += 1
            child = birth()
        c += k
    return c / num

def simulate_until_boy_girl(num):
    c = 0
    for _ in range(num):  
        k = 2
        child = birth()
        if child == 'girl':
            child = birth()
            while child != 'boy':
                k += 1
                child = birth()
        elif child == 'boy':
            child = birth()
            while child != 'girl':
                k += 1
                child = birth()
        c += k
    return c / num

num_sims = 100000

average_children_until_boy = simulate_until_boy(num_sims)
average_children_until_boy_girl = simulate_until_boy_girl(num_sims)

print("The average number of children there would be in a family if all people had children until they had a boy is:", average_children_until_boy)

print("The average number of children there would be in a family if all people had children until they had a boy and a girl is:", average_children_until_boy_girl)

