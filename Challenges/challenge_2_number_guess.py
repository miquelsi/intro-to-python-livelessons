"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random

print("I'm thinking of a number between 1 and 20")
answer = random.randint(1, 20)


def run_game(chances):
    guess = int(input("Make a guess ({} chances left): ".format(chances)))

    if guess == answer:
        print("You guessed right!")
        return True
    elif guess < answer:
        print("The number is higher")
    else:
        print("The number is lower")

    return False


chances = 3
while chances > 0:
    if run_game(chances) is True:
        break
    chances -= 1

if chances == 0:
    print("Game over! The number was " + str(answer))
