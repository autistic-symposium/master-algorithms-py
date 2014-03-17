#!/usr/bin/python3
# mari von steinkirch @2014
# steinkirch at gmail
# for hacker school application
'''
Write a program that prints out the numbers 1 to 100 (inclusive). If the number is divisible by 3, print Crackle instead of the number. If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop. 
'''


   
def CracklePop(n):
    for i in range(1, n+1): 
        if i%3 == 0 and i%5 == 0: print('CracklePop!!!')
        elif i%3 == 0: print("Crackle!!!")
        elif i%5 == 0: print("Pop!!!")
        else: print(i)
    		

def main():
    CracklePop(100)
        
                   
if __name__ == '__main__':
    main()

