#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def get_row(self, irow: int) -> list[int]:
        
        if irow == 0: 
            return [1]
	
        result = self.get_row(irow - 1)
        
        return [1] + [sum(_) for _ in zip(result, result[1:])] + [1]
