#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def dist_pow(a1, a2, b1, b2):
    set1 = set()
    for a in range(a1, a2 + 1):
        for b in range(b1, b2 + 1):
            set1.add(a**b)          
    return len(set1)

    
   

def main():
    import time
    start = time.time() 

    print(dist_pow(2, 5, 2, 5))    
    print(dist_pow(2, 100, 2, 100))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

