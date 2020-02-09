#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

'''
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''


def find_if_leap_year(y):
    if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
        return True
    return False

   
def counting_sundays():
    ''' define variables '''
    days_year = 7*31 + 4*30 + 28
    count_sundays = 0  
    days_week = 7 
    dict_week = {0: 'mon', 1:'tue', 2:'wed', 3:'thu', 4:'fri', 5:'sat', 6:'sun'} 
    
    
    ''' with info from 1900 find first day for 1901 '''
    first_day = days_year%days_week  # not a leap year
   
    for y in range (1901, 2001):
        leap_year = find_if_leap_year(y)
        days_count = first_day
               
        for m in range(1, 13):
            if days_count%7 == 6:
                count_sundays += 1             
            if m == 2:
                if leap_year:
                    days_count += 29
                else: 
                    days_count += 28
            elif m == 4 or m == 6 or m == 9 or m == 11:
                days_count += 30
            else:
                days_count += 31                  
                 
        if leap_year: first_day = (first_day +2)%days_week
        else: first_day = (first_day +1)%days_week
           
    return count_sundays
    
    

def main():
    print(counting_sundays())
    print('Tests Passed!')
                   
if __name__ == '__main__':
    main()

