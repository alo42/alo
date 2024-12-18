import random


def simulate_random_choice():
    return random.randint(1, 6)


def simulate_random_bullet():
    return random.randint(1, 6)


def simulate_different_bullet1(possible_bullets):
    return random.choice(possible_bullets)


def simulate_difbullet2(possible_bullets, bullet_1):
    if bullet_1 != 6 and bullet_1 != 1:
        possible_bullets.remove(bullet_1)
        possible_bullets.remove(bullet_1 + 1)
        possible_bullets.remove(bullet_1 - 1)
    elif bullet_1 == 6:
        possible_bullets.remove(bullet_1)
        possible_bullets.remove(bullet_1 - 1)
        possible_bullets.remove(1)
    elif bullet_1 == 1:
        possible_bullets.remove(bullet_1)
        possible_bullets.remove(bullet_1 + 1)
        possible_bullets.remove(6)
    bullet_2 = random.choice(possible_bullets)
    return bullet_2

def simulate_five_chamber_choice():
    return random.randint(1, 5)


def simulate_five_chamber_bullet():
    return random.randint(1, 5)

def simulate_five_chamber_different_bullet1(possible_bullets):
    return random.choice(possible_bullets)

def simulate_five_chamber_different_bullet2(possible_bullets, bullet_1):
    if bullet_1 != 5 and bullet_1 != 1:
        possible_bullets.remove(bullet_1)
        possible_bullets.remove(bullet_1 + 1)
        possible_bullets.remove(bullet_1 - 1)
    elif bullet_1 == 5:
        possible_bullets.remove(bullet_1)
        possible_bullets.remove(bullet_1 - 1)
        possible_bullets.remove(1)
    elif bullet_1 == 1:
        possible_bullets.remove(bullet_1)
        possible_bullets.remove(bullet_1 + 1)
        possible_bullets.remove(5)
    bullet_2 = random.choice(possible_bullets)
    return bullet_2


try:
    num_games = int(input("Number of games: "))

    #  6 chamber with adjacent bullets
    adj_spin_wc = 0
    for i in range(1, num_games + 1):
        bullet1 = simulate_random_bullet()
        if bullet1 == 6:
            bullet2 = 1
        else:
            bullet2 = bullet1 + 1
        x = simulate_random_choice()
        if x != bullet1 and x != bullet2:
            adj_spin_wc += 1
    total_games1 = num_games
    print("Probability 6 chamber adjacent spin:", adj_spin_wc / total_games1)

    #  6-chamber non-adjacent bullets
    non_adj_spin_games = 0
    adj_no_spin = 0
    for i in range(1, num_games):
        bullet1 = simulate_random_bullet()
        x = 0
        if bullet1 == 6:
            bullet2 = 1
        else:
            bullet2 = bullet1 + 1
        x1 = simulate_random_choice()
        x = x1 + 1
        if x == 7:
            x = 1
        if x1 == bullet1 or x1 == bullet2:
            non_adj_spin_games += 1
            continue
        elif x != bullet1:
            adj_no_spin += 1

    total_games2 = num_games - non_adj_spin_games
    print("Probability 6 chamber adjacent no spin:", adj_no_spin / total_games2)

    # 6chamber non-adjacent bullets
    non_adj_spin = 0
    for i in range(1, num_games):
        bullets_possible = [1, 2, 3, 4, 5, 6]
        bullet1 = simulate_different_bullet1(bullets_possible)
        bullet2 = simulate_difbullet2(bullets_possible, bullet1)
        x = simulate_random_choice()
        if x != bullet1 and x != bullet2:
            non_adj_spin += 1
    total_games3 = num_games
    print("Probability 6 chamber non-adjacent spin:", non_adj_spin / total_games3)

    #  6 chamber revolver with non-adjacent bullets and no spin
    non_adj_no_spin_games = 0
    non_adj_spin = 0
    for i in range(1, num_games):
        y = 0
        bullets_possible = [1, 2, 3, 4, 5, 6]
        bullet1 = simulate_different_bullet1(bullets_possible)
        bullet2 = simulate_difbullet2(bullets_possible, bullet1)
        x1 = simulate_random_choice()
        y = x1 + 1
        if y == 6:
            y = 1
        if x1 == bullet1 or x1 == bullet2:
            non_adj_no_spin_games += 1
            continue
        elif y != bullet1 and y != bullet2:
            non_adj_spin += 1
    total_games3 = num_games - non_adj_no_spin_games
    print("Probability 6 chamber non-adjacent no spin:", non_adj_spin / total_games3)

    # Simulation for a 5-chamber revolver with adjacent bullets
    five_adj_spin = 0
    for i in range(1, num_games):
        bullet1 = simulate_five_chamber_bullet()
        if bullet1 == 5:
            bullet2 = 1
        else:
            bullet2 = bullet1 + 1
        x = simulate_five_chamber_choice()
        if x != bullet1 and x != bullet2:
            five_adj_spin += 1
    five_total_games_1 = num_games
    print("Probability 5 chamber adjacent spin:", five_adj_spin / five_total_games_1)

    # Simulation for a 5-chamber revolver with non-adjacent bullets
    five_non_adj_spin_games = 0
    five_adj_no_spin = 0
    for i in range(1, num_games):
        bullet1 = simulate_five_chamber_bullet()
        x = 0
        if bullet1 == 5:
            bullet2 = 1
        else:
            bullet2 = bullet1 + 1
        x1 = simulate_five_chamber_choice()
        x = x1 + 1
        if x == 6:
            x = 1
        if x1 == bullet1 or x1 == bullet2:
            five_non_adj_spin_games += 1
            continue
        elif x != bullet1 and x != bullet2:
            five_adj_no_spin += 1

    five_total_games2 = num_games - five_non_adj_spin_games
    print("Probability 5 chamber adjacent no spin:", five_adj_no_spin / five_total_games2)

    # Simulation for a 5-chamber revolver with non-adjacent bullets
    five_non_adj_spin = 0
    for i in range(1, num_games):
        bullets_possible = [1, 2, 3, 4, 5]
        bullet1 = simulate_five_chamber_different_bullet1(bullets_possible)
        bullet2 = simulate_five_chamber_different_bullet2(bullets_possible, bullet1)
        x = simulate_five_chamber_choice()
        if x != bullet1 and x != bullet2:
            five_non_adj_spin += 1
    five_total_games3 = num_games
    print("Probability 5 chamber non-adjacent spin:", five_non_adj_spin / five_total_games3)

    # Simulation for a 5-chamber revolver with non-adjacent bullets and no spin
    five_non_adj_no_spin_games = 0
    five_non_adj_spin = 0
    for i in range(1, num_games):
        bullets_possible = [1, 2, 3, 4, 5]
        bullet1 = simulate_five_chamber_different_bullet1(bullets_possible)
        bullet2 = simulate_five_chamber_different_bullet2(bullets_possible, bullet1)
        x = simulate_five_chamber_choice()
        if x == 5:
            x = 1
        if x == bullet1 or x == bullet2:
            five_non_adj_no_spin_games += 1
            continue
        elif x + 1 != bullet1 and x + 1 != bullet2:
            five_non_adj_spin += 1
    five_total_games4 = num_games - five_non_adj_no_spin_games
    print("Probability 5 chamber non-adjacent no spin:", five_non_adj_spin / five_total_games4)

except ValueError:
    print("You must enter only integers!")
