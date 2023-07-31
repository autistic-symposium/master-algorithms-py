#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


   
def special_pyt(n):
    for i in range(3, n):
        for j in range(i+1, n):
            c = calc_c(i,j)
            if i + j + c == n: 
                return i*j*c

def calc_c(a, b):
    return (a**2 + b**2)**0.5

    

def main():
    assert(special_pyt(3+4+5) == (3*4*5))
    print(special_pyt(1000))
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

