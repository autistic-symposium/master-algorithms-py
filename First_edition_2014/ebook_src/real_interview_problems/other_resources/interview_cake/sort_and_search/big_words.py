#!/bin/python

"""
I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, looking for words I didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory. When I reached the end of the dictionary, I started from the beginning and did the same thing until I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words, this is an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.
"""

def find_index(words):

    for i, word in enumerate(words):
        if word[0] > words[i+1][0]:
            return i+1, words[i+1]

    return "Not found"



def find_index_bs(words):
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        guess_index = floor_index + ((ceiling_index - floor_index) / 2)

        if words[guess_index] >= first_word:
            floor_index = guess_index
        else:
            ceiling_index = guess_index

        if floor_index + 1 == ceiling_index:
            return ceiling_index


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', 
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print find_index(words)
print
print find_index_bs(words)