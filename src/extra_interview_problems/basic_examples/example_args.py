#!/usr/bin/python

def simple2(a, *args):
    print args

def simple(*args):
    print args

def simple3(**kwargs):
    print kwargs


simple(1, 2, 3)
simple2(1, 2, 3)
simple3(x=1, y=2)


def logger(func):
    def inner(*args): #1
        print "Arguments were: {0}".format(args)
        return func(*args)
    return inner

@logger
def foo(x, y):
    return x+y

print foo(1, 2)