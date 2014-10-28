#!/usr/bin/python
#
''' give all the combinations of a str or list '''


def comb_str(l1):
    if len(l1) < 2:
        return l1
    result = []
    for i, c in enumerate(l1):
        result.append(c)
        for comb in comb_str(l1[i+1:]):
            result.append(c + "".join(comb))
    return result



if __name__ == '__main__':
    l1 = ['a', 'b', 'c']
    print comb_str(l1)
