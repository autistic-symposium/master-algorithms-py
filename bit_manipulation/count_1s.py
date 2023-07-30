def count_ones(n: int) -> int:
        
        counter = 0
        
        while n:
            
            if n & 1:
                counter += 1
            
            n >>= 1
        
        return counter
