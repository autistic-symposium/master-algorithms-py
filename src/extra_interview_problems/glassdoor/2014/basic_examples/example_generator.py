#!/usr/bin/env python

__author__ = "bt3"

" Example of generator."

def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]

if __name__ == '__main__':
    for c in reverse('awesome'):
        print c