#!/bin/python

''' Check if palindrome'''


def check_pal(string):
    string = "".join(string.split(' '))
    p1, p2 = 0, len(string)-1
    pal = True
    while p1 < p2:
        if string[p1] != string[p2]:
            pal = False
            break
        p1+=1
        p2-=1
    return pal


def check_pal2(string):
    string = "".join(string.split(' '))
    if len(string)<2:
        return True
    if string[0] != string[-1]:
        return False
    return check_pal2(string[1:-1])


if __name__ == '__main__':
    string1 = "borrow or rob"
    string2 = " draw ward"
    string3 = "google is fun"
    print(check_pal(string1))
    print(check_pal(string2))
    print(check_pal(string3))
    print
    print(check_pal2(string1))
    print(check_pal2(string2))
    print(check_pal2(string3))