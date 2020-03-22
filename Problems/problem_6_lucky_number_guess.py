"""
Guess the number between 1 and 10
"""

import random
answer = random.randint(1, 10)

guess = int(input("I'm thinking of a number between 1 and 10: "))

# If the number is correct, tell the user
# Otherwise, tell them if the answer is higher or lower than their guess
if answer == guess:
    print("It is correct!")
elif guess < answer:
    print("No, it's higher")
else:
    print("No, it's lower")

print('The number was {}'.format(answer))
