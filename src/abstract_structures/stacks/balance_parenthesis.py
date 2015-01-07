#!/usr/bin/env python

__author__ = "bt3"

''' use a stack to balance the parenteses of a string '''


from stack import Stack

def balance_par_str_with_stack(str1):

    s = Stack()
    balanced = True
    index = 0

    while index < len(str1) and balanced:

        symbol = str1[index]

        if symbol == "(":
            s.push(symbol)

        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True

    else:
        return False



if __name__ == '__main__':
    print(balance_par_str_with_stack('((()))'))
    print(balance_par_str_with_stack('(()'))
