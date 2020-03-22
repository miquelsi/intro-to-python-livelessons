"""
Deal a hand of 5 cards
"""
import random

suits = ['♠︎', '♣︎', '♥︎', '♦︎']
values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']

cards = []
for suit in suits:
    for value in values:
        cards.append(suit + value)

hand = []

while len(hand) < 5:
    card = random.choice(cards)
    if not card in hand:
        hand.append(card)

print(hand)
