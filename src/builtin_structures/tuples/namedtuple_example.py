#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from collections import namedtuple

def  namedtuple_example():
    ''' show some examples for namedtuple '''
    sunnydale = namedtuple('name', ['job', 'age'])
    buffy = sunnydale('slayer', '17')
    print(buffy.job)


if __name__ == '__main__':
    namedtuple_example()


