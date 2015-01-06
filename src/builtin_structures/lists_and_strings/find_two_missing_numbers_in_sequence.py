#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail


import math

def find_two_missing_numbers(l1):
    """ Two numbers out of n numbers from 1 to n are missing. The remaining n-2 numbers are in the      
    array but not sorted. Find the missing numbers The sum1 is the sum of all the elements in n. The 
    sum2 is the sum of all the elements in n-2. sum1 - sum2 = num1 + num2 = s. The prod1 is the prod of 
    all the elements in n. The prod2 is the prod of all the elements in n-2. prod1/prod2 = num1*num2 = 
    p. Runtime is O(n), because it scan 3 times. Space is O(1)
    
    - In case of finding one integer,  Let the missing number be M. We know that the sum of first N 
    natural numbers is N*(N+1)/2. Traverse through the array once and calculate the sum. This is the 
    sum of first N natural numbers – M or S=N*(N+1)/2 – M. Therefore M = N*(N+1)/2 – S.
    """
    
    n_min_2 = len(l1)
    n = n_min_2 + 2
    sum1, sum2, prod1, prod2 = 0,0,1,1
    sum2 = sum(l1[:])
    sum1 = sum(range(1,n+1))
    s = sum1 - sum2
    
    for i in range(1, n-1): 
        prod1 = prod1*i
        prod2 = prod2*l1[i-1]
        
    prod1 = prod1*n*(n-1)
    p = prod1/prod2
    num1 =  (s + math.sqrt(s*s - 4*p))/2
    num2 =  (s - math.sqrt(s*s - 4*p))/2
   
    return num1, num2



def test_find_two_missing_numbers():
    l1 = [1, 3, 5]
    result = find_two_missing_numbers(l1)
    assert(result[0] == 2.0 or result[0] == 4.0)
    print('Tests passed!')


if __name__ == '__main__':
    test_find_two_missing_numbers()







