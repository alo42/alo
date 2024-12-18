import random

initialBet = 1
maxRounds = 50
winsNeeded = 5
lossesNeeded = 5

fibonacciSequence = [1, 1]
betIndex = 0
totalProfit = 0
roundsPlayed = 0
wins = 0
losses = 0

while roundsPlayed < maxRounds and wins < winsNeeded and losses < lossesNeeded:
    roundsPlayed += 1
    result = random.choice(['red', 'black'])
    
    bet = fibonacciSequence[betIndex]

    if result == 'red':
        totalProfit += bet
        wins += 1
        betIndex = max(0, betIndex - 2)
    else:
        totalProfit -= bet
        losses += 1
        betIndex = min(len(fibonacciSequence) - 1, betIndex + 1)
        
    if betIndex == len(fibonacciSequence) - 1:
        fibonacciSequence.append(fibonacciSequence[-1] + fibonacciSequence[-2])

print(f"rounds: {roundsPlayed}")
print(f"wins: {wins}")
print(f"losses: {losses}")
print(f"pprofit: ${totalProfit}")
