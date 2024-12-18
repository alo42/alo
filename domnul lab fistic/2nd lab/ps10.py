import random

def ride(num):
    amount_paid = 0
    k = 0

    for _ in range(num):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        if a <= 5:
            k += 1
        if b <= 2:
            amount_paid += 6
    if k >= 1:
        amount_paid += 50
    if k >= 2:
        amount_paid += 200
    if k >= 3:
        for _ in range(k-2):
            amount_paid += 300
    return amount_paid

def simulation(num):
    a = 0
    for _ in range(num):
        a += ride(730)
    return a/num

pay_troleu = 730*6
dont_pay = simulation(1000)

print(f"The amount paid by us is {pay_troleu} and the amount paid by Jora Petrovici is {dont_pay}")