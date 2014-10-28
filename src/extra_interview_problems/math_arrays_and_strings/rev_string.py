#!/bin/python

''' Reverting a string '''


def revert(string):
    return string[::-1]


if __name__ == '__main__':
    string = "Google is fun!"
    print(revert(string))