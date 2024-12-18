import random

def play_game():
    X = random.uniform(0, 1)
    i = 1
    while True:
        Y = random.uniform(0, 1)
        if Y > X:
            return i - 1
        i += 1

def simulate(num_games):
    total_payout = 0
    for _ in range(num_games):
        total_payout += play_game()
    return total_payout / num_games

num_games = 10000
fair_entrance_fee = simulate(num_games)

print(f"{fair_entrance_fee:.4f}")
