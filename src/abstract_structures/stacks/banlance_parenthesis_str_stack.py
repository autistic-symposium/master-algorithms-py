#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from stack import Stack

def balance_par_str_with_stack(symbolString):
    ''' use a stack to balance the parenteses of a string '''
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
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




def test_balance_par_str_with_stack(module_name='this module'):
    print(balance_par_str_with_stack('((()))'))
    print(balance_par_str_with_stack('(()'))
        
    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_balance_par_str_with_stack()
