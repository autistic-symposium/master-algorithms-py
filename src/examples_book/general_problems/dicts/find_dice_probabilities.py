#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

from collections import Counter, defaultdict

def find_dice_probabilities(S, n_faces=6):
    ''' given 2 dice, determine number of ways to sum S if all dice are rolled '''
    
    if S > 2*n_faces or S < 2: return None       
    
    cdict = Counter()
    ddict = defaultdict(list)
      
    for dice1 in range(1, n_faces+1):
        for dice2 in range(1, n_faces+1):
            t = [dice1, dice2]
            cdict[dice1+dice2] += 1
            ddict[dice1+dice2].append( t)       

    return [cdict[S], ddict[S]]


def test_find_dice_probabilities(module_name='this module'):
    n_faces = 6
    S = 5
    results = find_dice_probabilities(S, n_faces)
    print(results)
    assert(results[0] == len(results[1]))


if __name__ == '__main__':
    test_find_dice_probabilities()
