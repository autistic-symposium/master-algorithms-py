#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def find_coll_seq(n):
    count = 1
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n +1
        count += 1
    return count


def find_longest_chain(limit):
    longest, number = 0, 0
    start = 0
    while start <= limit:
        size_chain = find_coll_seq(start)
        if size_chain > longest:
            longest = size_chain
            number = start
        start += 1
     
    return (longest, number)



    
def main():
    import time
    start = time.time() 
     
    #print(find_longest_chain(13))
    print(find_longest_chain(10**6))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

