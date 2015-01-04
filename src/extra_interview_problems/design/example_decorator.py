#!/usr/bin/python


# testing generator

def interate(x):
    for i in range(x):
        yield i

a =  interate(10)

print a.next()
print a.next()
print a.next()

# testing decorator

def sum(func):
    s = 0
    for i in func():
        s += i
    return s

@sum
def interate():
    a = []
    for i in range(10):
        a.append(i)
    return a

print interate

def interate():
    a = []
    for i in range(10):
        a.append(i)
    return a

print sum(interate)
