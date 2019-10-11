#!/bin/python

"""
Write a function to tell us if a full deck of cards shuffled_deck is a single riffle of two other halves half1 and half2.

We'll represent a stack of cards as a list of integers in the range 1..521..52 (since there are 5252 distinct cards in a deck).
Why do I care? A single riffle is not a completely random shuffle. If I'm right, I can make more informed bets and get rich and finally prove to my ex that I am not a "loser with an unhealthy cake obsession" (even though it's too late now because she let me go and she's never getting me back).
"""

def is_single_riffle(half1, half2, shuffled_deck,
                     shuffled_deck_index=0, half1_index=0, half2_index=0):
    if shuffled_deck_index == len(shuffled_deck):
        return True

    if ((half1_index < len(half1)) and
            half1[half1_index] == shuffled_deck[shuffled_deck_index]):
        half1_index += 1

    elif ((half2_index < len(half2)) and
            half2[half2_index] == shuffled_deck[shuffled_deck_index]):
        half2_index += 1
    else:
        return False

    shuffled_deck_index += 1
    return is_single_riffle(
        half1, half2, shuffled_deck, shuffled_deck_index,
        half1_index, half2_index)