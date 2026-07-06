#!/usr/bin/python3

# <m+B> to mark this line

# this file is made with ai
import random

def n(msg, mn=1):
    while True:
        try:
            x = int(input(msg))
            if x >= mn:
                return x
        except ValueError:
            pass
        print(f"Enter {mn} or higher.")

def game():
    print("Guessing Game")
    mode = n("1 = turn by turn, 2 = shared hints: ", 1)
    players = [f"Player {i}" for i in range(1, n("How many players? ", 1) + 1)]
    rounds = n("Rounds: ", 1)
    max_num = n("Highest number: ", 2)
    lives = n("Lives: ", 1)
    scores = {p: 0 for p in players}

    for r in range(1, rounds + 1):
        print(f"\nRound {r}")
        secret = random.randint(1, max_num)
        low, high = 1, max_num

        for p in players:
            print(f"\n{p}")
            tries = lives
            while tries:
                if mode == 2:
                    print(f"Hint: {low} to {high}")
                guess = n("Guess: ", 1)

                if guess == secret:
                    print("Correct!")
                    scores[p] += 3
                    break

                scores[p] += 1
                tries -= 1

                if guess < secret:
                    print("Too low.")
                    low = max(low, guess + 1)
                else:
                    print("Too high.")
                    high = min(high, guess - 1)

                print(f"Lives left: {tries}")

            if guess != secret:
                print(f"The number was {secret}")

    print("\nScores")
    for p, s in scores.items():
        print(p, s)

    best = max(scores.values())
    winners = [p for p, s in scores.items() if s == best]
    print("Winner:", ", ".join(winners))

while True:
    game()
    if input("\nPlay again? (y/n): ").lower() != "y":
        break
