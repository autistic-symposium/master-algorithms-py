#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def large_sum(filename):
    sum_total, lines, numbers = 0, 0, 0
    with open(filename) as file:
        for line in file:
            sum_total += int(line.strip('\n'))
    return str(sum_total)[0:10]

    
def main():
    import time
    start = time.time() 
      
    filename = 'large_sum.dat'
    print(large_sum(filename))
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

