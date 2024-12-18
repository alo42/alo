import random
import matplotlib.pyplot as plt

def roll_three_dice():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

def simulate_rolls(num_rolls):
    sums = {i: 0 for i in range(3, 19)}  
    for _ in range(num_rolls):
        roll_sum = roll_three_dice()
        sums[roll_sum] += 1
    return sums


num_rolls = 100000


sums = simulate_rolls(num_rolls)


print(f"Frequency of 9: {sums[9]}")
print(f"Frequency of 10: {sums[10]}")

plt.bar(sums.keys(), sums.values())
plt.xlabel('Sum of Dice Rolls')
plt.ylabel('Frequency')
plt.title('Frequency of Different Dice Sums (3 Dice Rolls)')
plt.show()
