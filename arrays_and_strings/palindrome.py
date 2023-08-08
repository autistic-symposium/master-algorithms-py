#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def is_palindrome(sentence):

    sentence = sentence.strip(' ')
    if len(sentence) < 2:
        return True
    
    if sentence[0] == sentence[-1]:
        return is_palindrome(sentence[1:-1])
    
    return False
