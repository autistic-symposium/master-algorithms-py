#!/bin/python

"""
Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're using an algorithm that sorts in O(n\lg{n})O(nlgn) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.

Write a function that takes:

a list of unsorted_scores
the highest_possible_score in the game
and returns a sorted list of scores in less than O(n\lg{n})O(nlgn) time.
"""

def sort_scores(unsorted_scores, highest_score):

    score_counts = [0] * (highest_score+1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []

    for score in range(len(score_counts)-1, -1, -1):
        count = score_counts[score]

        for i in range(count):
            sorted_scores.append(score)

    return sorted_scores



if __name__ == '__main__': 

    unsorted_scores = [37, 89, 41, 65, 91, 53]
    HIGHEST_POSSIBLE_SCORE = 100

    print sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
