#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

def find_majority_in_seq(seq):
    ''' find value which occurrence is greater than the total occurrence of all other elements '''
    times = 1
    result = seq[0]
    for i in range(len(seq)):
        if times == 0:
            result = seq[i]
            times = 1
        elif seq[i] == result:
            times +=1
        else:
            times -=1
            
    if times == 0: return None
    else:
        count = 0
        for i, c in enumerate(seq):
            if c == result: 
                count += 1
        return result, count 


def test_find_majority_in_seq():
    seq = [1, 1, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6]
    seq2 = [1, 2, 3]
    assert(find_majority_in_seq(seq) == (4, 4))
    assert(find_majority_in_seq(seq2) == None)
    print('Tests passed!')

if __name__ == '__main__':
    test_find_majority_in_seq()



    
    
    
    


"""
>>> A = [1, 2, 3, 2, 2, 4, 2, 5, 2]
>>> find_majority(A)
(2, 5)
>>> A = [1]
>>> find_majority(A)
(1, 1)
>>> A = [1, 2, 3, 2, 5, 6, 7]
>>> find_majority(A)
No Majority Element.
"""



