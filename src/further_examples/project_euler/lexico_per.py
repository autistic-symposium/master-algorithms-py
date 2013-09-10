#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def perm_item(elements):
    if len(elements) <= 1:
        yield elements  
    else:
        for (index, elmt) in enumerate(elements):
            other_elmts = elements[:index]+elements[index+1:]
            for permutation in perm_item(other_elmts): 
                yield [elmt] + permutation


def lex_perm(l1, n):
    perm_list = list(perm_item(l1))
    return sorted(perm_list)[n-1]


def main():
    import time
    start = time.time() 
    
    l1 = [0,1,2,3,4,5,6,7,8,9]
    n = 10**6
    print(lex_perm(l1, n))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

