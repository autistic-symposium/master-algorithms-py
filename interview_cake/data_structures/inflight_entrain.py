#!/bin/python

"""
Users on longer flights like to start a second movie right when their first one ends, 
but they complain that the plane usually lands before they can see the ending. 
So you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a 
list of integers movie_lengths (in minutes) and returns a boolean indicating 
whether there are two numbers in movie_lengths whose sum equals flight_length.

When building your function:

Assume your users will watch exactly two movies
Don't make your users watch the same movie twice
Optimize for runtime over memory
"""

def is_there_two_movies(flight_length, movie_lengths):
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    return False



if __name__ == '__main__':

    flight_length = 10

    movie_lengths = [2, 4, 7]
    print(is_there_two_movies(flight_length, movie_lengths))
    print("Should be True")

    movie_lengths = [5, 6, 7, 8]
    print(is_there_two_movies(flight_length, movie_lengths))
    print("Should be False")