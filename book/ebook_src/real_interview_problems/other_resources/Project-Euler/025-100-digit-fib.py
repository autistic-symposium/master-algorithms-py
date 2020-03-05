#!/usr/bin/python3
# mari wahl @2014
# marina.w4hl at gmail
#

'''
The Fibonacci sequence is defined by the recurrence relation:
 Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
 Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
Answer: 4782
'''


def fib(num=1, num_before=1):
  found = False

  num_before, num = num, num + num_before

  if count_digits(num) == 1000: found = True

  return num, num_before, found



def count_digits(num):
  num_str = str(num)
  return len(num_str)



def main():
  found = False
  num = 1
  num_before = 1
  count = 2

  while not found:
    num, num_before, found = fib(num, num_before)
    count +=1

  print(count)
  print('Done!')

if __name__ == '__main__':
  main()


