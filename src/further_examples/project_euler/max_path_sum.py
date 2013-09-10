#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def max_path_sum(t):
    root = t[0][0]
    height, width, index, large_num = 1, 0, 0, 0
    max_sum = root
    heights = len(t[:])
    
    while height < heights:      
        values_here = t[height][index:index+2]
        if values_here[0] > values_here[1]:
            large_num = values_here[0]
        else:
            large_num = values_here[1]
            index += 1
        max_sum += large_num
        pivot = large_num
        width, large_num = 0, 0
        height += 1
    
    return max_sum

def edit_input(filename):
    output = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip('\n')
            output.append(line.split(' '))
    for i, l1 in enumerate(output):
        for j, c in enumerate(output[i]):
            output[i][j] = int(c)
    return(output)



def main():
    import time
    start = time.time() 
    
    filename = 'max_path_sum0.dat'
    t1 = edit_input(filename)
    print('Little pir: ',max_path_sum(t1))
    
    filename = 'max_path_sum.dat'
    t2 = edit_input(filename)
    print('Big pir: ', max_path_sum(t2))    
    
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

