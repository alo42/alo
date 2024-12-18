import random

initialBet = 1
maxRounds = 50
winsNeeded = 5

bet = initialBet
roundsPlayed = 0
wins = 0
totalProfit = 0

while roundsPlayed < maxRounds and wins < winsNeeded:
    roundsPlayed += 1
    result = random.choice(['red', 'black'])

    if result == 'red':
        totalProfit += bet
        wins += 1
        bet = max(1, bet - 1)
    else:
        totalProfit -= bet
        bet += 1

print(f"rounds: ${roundsPlayed}")
print(f"wins: ${wins}")
print(f"profit: ${totalProfit}")
