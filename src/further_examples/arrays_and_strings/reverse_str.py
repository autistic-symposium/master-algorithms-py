#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

   
def reverse_str(s):
    ''' in place '''
    sr_ls = []
    for i in range(len(s)-1, -1, -1):
        sr_ls.append(s[i])
    return ''.join(sr_ls)
        



def main():
    s1 = 'abcdefg'
    s2 = 'buffy'
    s3 = ''
    print(reverse_str(s1))
    print(reverse_str(s2))
    print(reverse_str(s3))
                   
if __name__ == '__main__':
    main()

