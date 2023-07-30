#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

# Given a square matrix, calculate the absolute difference 
# between the sums of its diagonals.

import math
import os
import random
import re
import sys

def diagonal_difference(arr):

    diag_1 = 0
    diag_2 = 0
    
    i, j = 0, len(arr) - 1
    
    while i < len(arr) and j >= 0:
        
        diag_1 += arr[i][i]
        diag_2 += arr[i][j]
        i += 1
        j -= 1
        
    return diag_1, diag_2, abs(diag_1 - diag_2)
            
            

if __name__ == '__main__':
    
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonal_difference(arr))
