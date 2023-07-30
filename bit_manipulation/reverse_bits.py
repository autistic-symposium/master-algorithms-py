def reverse_bits(n: int) -> int:
        
        result, base = 0, 31
        
        while n:
            result += (n & 1) << base
            n >>= 1
            base -= 1
        
        return result
