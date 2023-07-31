#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

   
def even_fib_num(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def main():
    print(sum(n for n in even_fib_num(4e6) if not (n & 1)))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

