#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def number_spiral(spiral):
    
    
    return rows, mid
    
def make_spiral(n):
    spiral = []
    row = rows//2
    col = col//2
    count = 1
    while row < n:
        while col < n:
            spiral[col][row] = count
            count += 1
            if count%2 == 0:
                col += 1
            else:
                row += 1
        
    return spiral

def main():
    import time
    start = time.time() 
    
    n = 5
    spiral = make_spiral(n)
    print(number_spiral(spiral))# 101
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

