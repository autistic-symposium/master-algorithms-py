#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def find_sum_proper_div(n):
    sum_proper_div = 0
    for i in range(1, n):
        if n%i == 0:
            sum_proper_div += i
    return sum_proper_div     
   
   
def find_all_abund(n):
    sum_div_list = [find_sum_proper_div(i) for i in range(n)]
    abu = set()
    for i in range(n):
        if i < sum_div_list[i]:
            abu.add(i)
    return abu
      
   
def non_abund_sums(n):
    abu = find_all_abund(n)  
    sum_nom_abu = 0  
    
    for i in range(n):
        if not any( (i-a in abu) for a in abu):
            sum_nom_abu += i       
       
    return sum_nom_abu 
    
    
def test_(): 
    r = set([i for i in range(25)])
    r_abu = {24}
    r = r - r_abu
    assert(non_abund_sums(25) == sum(r)) 
    print(non_abund_sums(28123))
    print('Tests Passed!')
            
            
if __name__ == '__main__':
    test_()

