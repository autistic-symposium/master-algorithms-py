def find_product_without_division(seq):
    '''Given an array of numbers, replace each number with the product of all the numbers in the array except the number itself *without* using division '''
    forw = []
    bacw = []
    
    for i in range(len(seq)):
        prod_f = 1
        prod_b = 1
        for next in range(i+1, len(seq)):
            prod_f *= seq[next]
        for before in range(0, i):
            prod_b *= seq[before]
        forw.append(prod_f)
        bacw.append(prod_b)
        
    print(bacw)
    print(forw)  
    for i in range(len(seq)):
        seq[i] = forw[i]*bacw[i]
    
    return seq
    
    

def test_find_product_without_division():
    seq = [2,3,4]
    result = [12, 8, 6]
    print(find_product_without_division(seq))

    
    
if __name__ == '__main__':
    test_find_product_without_division()
