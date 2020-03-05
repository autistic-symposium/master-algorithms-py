#!/usr/bin/python3
# mari wahl @2014
# marina.w4hl at gmail


'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10  =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Answer: 983
'''


def recurring_cycle(n, d):
    for dd in range(1, d):
        if 1 == 10**dd % d:
            return dd
    return 0

def main():
  n = 1
  limit = 1000
  longest = max(recurring_cycle(n, i) for i in range(2, limit+1))
  print [i for i in range(2, limit+1) if recurring_cycle(n, i) == longest][0]

if __name__ == '__main__':
    main()

