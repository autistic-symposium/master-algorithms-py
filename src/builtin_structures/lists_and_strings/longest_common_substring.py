#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



def longest_common_substring(str1, str2):
    ''' find the largest commom substring from 2 strings '''
    m = [[0 for i in range(len(str2) + 1)] for k in range(len(str1) + 1)]
    lcs = None
    max_len = 0
    for y in range(1, len(str1) + 1):
        for x in range(1, len(str2) + 1):
            m[y][x] = m[y - 1][x - 1] + 1 if (str1[y - 1] == str2[x - 1]) else 0

            if m[y][x] > max_len:
                max_len = m[y][x]
                lcs = str1[(y - max_len):y]
    return max_len, lcs   
    

def test_longest_common_substring():
    str1 = 'buffy is a vampire slayer'
    str2 = 'aaas bampires vslay'
    assert(longest_common_substring(str1, str2) == (6, 'ampire'))
    print('Tests passed!')


if __name__ == '__main__':
    test_longest_common_substring()


