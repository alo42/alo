import random

sims = 10000  
totalWinnings = 0

for _ in range(sims):
    tossCount = 1
    while random.choice(['H', 'T']) != 'H':  
        tossCount += 1
    totalWinnings += 2 ** tossCount 

expVal = totalWinnings / sims  
print(expVal)
