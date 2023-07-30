#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

# find the length of the longest substring without repeating characters


def length_longest_substring(s: str) -> int:
        
        result = ""
        this_longest_string = ""
        
        i = 0
        
        for c in s:
            
            j = 0
        
            # this loop breaks if repeated
            while j < len(this_longest_string):
                
                if c == this_longest_string[j]:
                    if len(this_longest_string) > len(result):
                        result = this_longest_string
                    this_longest_string = this_longest_string[j+1:]
                    
                j += 1
            
            # this loop continues creating the string
            this_longest_string += c
                
            
        return result, this_longest_string
            
                

if __name__ == "__main__":
    s = "abcabcbb"
    print(length_longest_substring(s))

    s = "dvdf"
    print(length_longest_substring(s))
