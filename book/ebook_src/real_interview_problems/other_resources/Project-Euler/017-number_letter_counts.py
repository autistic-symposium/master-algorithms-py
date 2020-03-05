#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail



def number_letter_counts(n):
    dict_lett = build_dict(n)
    sum_letter = 0
    for item in dict_lett:
        sum_letter += dict_lett[item]
    return sum_letter 


def build_dict(n):
    lett_dict = {}
    numbers = (x for x in range(1, n+1))
    dec = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    ties = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    for number in numbers:
        if 1 <= number < 20:
            lett_dict[number] = len(dec[number-1])
        elif 20 <= number < 100:
            index_dec = number//10
            index_num = number%10 
            if index_num == 0:
                lett_dict[number] = len(ties[index_dec-2])
            else:
                lett_dict[number] =  len(ties[index_dec-2])  +  len(dec[index_num-1])
        elif 100 <= number < 1000:
            index_hun = number//100
            index_dec = number%100
            if index_dec == 0:
                lett_dict[number] = len(dec[index_hun-1]) + len('hundred')
            else:
                if 1 <= index_dec < 20:
                    lett_dict[number] = len(dec[index_hun-1]) + len('hundred') + len('and') +  len(dec[index_dec-1])
                elif  20 <= index_dec  < 100:
                    index_dec2 = index_dec//10
                    index_num = index_dec%10 
                    if index_num == 0:
                        lett_dict[number] = len(dec[index_hun-1]) + len('hundred') + len('and') +  len(ties[index_dec2-2])
                    else:
                        lett_dict[number] = len(dec[index_hun-1]) + len('hundred') + len('and') +  len(ties[index_dec2-2]) +  len(dec[index_num-1])
        elif number == 1000:
            lett_dict[number] = len('onethousand')
            
    return lett_dict
                
    
def main():
    import time
    start = time.time() 
      
    assert(number_letter_counts(5) == 19)
    print(number_letter_counts(1000))
    elapsed = (time.time() - start)
    print('Tests Passed!\n It took %s seconds to run them.' % (elapsed))   
                   
if __name__ == '__main__':
    main()

