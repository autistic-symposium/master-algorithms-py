#!/usr/bin/env python

__author__ = "bt3"



''' Reverting a string '''


def revert(string):
    return string[::-1]


if __name__ == '__main__':
    string = "Google is fun!"
    print(revert(string))