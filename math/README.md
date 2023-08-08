## math

<br>

* when dealing with floating point numbers, take note of rounding mistakes. consider using epsilon comparisons instead of equality checks (`abs(x - y) <= 1e-6` instead of `x == y`).

<br>

---

### fibonnaci

<br>

* check the dynamic programming chapter to learn how to solve this with memoization.

<br>

```python
def fibonacci(n):

    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

<br>

---

### determine whether a sudoku board is valid

<br>


<br>

```python

'''
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''

def is_valid_sudoku(board) -> bool:
        
  N = 9

  rows = [set() for _ in range(N)]
  cols = [set() for _ in range(N)]
  boxes = [set() for _ in range(N)]
            
  for r in range(N):
    for c in range(N):
      val = board[r][c]
      if val == '.':
        continue
                
      if val in rows[r]:
        return False
      rows[r].add(val)

      if val in cols[c]:
        return False
      cols[c].add(val)

      index = (r // 3) * 3 + c // 3
      if val in boxes[index]:
        return False
      boxes[index].add(val)
        
  return True

```

<br>

---

### check if happy number

<br>

```python
def get_next(n):
  
  total_sum = 0
  while n > 0:
    n, digit = divmod(n, 10)
    total_sum += digit**2

  return total_sum


def is_happy(self, n: int) -> bool:

  seen = set()
  while n != 1 and n not in seen:
    seen.add(n)
    n = get_next(n)

  return n == 1
```


<br>

---

### get a row in a pascal triangle

<br>

```python
def get_row(self, row: int) -> list[int]:
        
        if row == 0: 
            return [1]
	
        result = self.get_row(row - 1)
        
        return [1] + [sum(_) for _ in zip(result, result[1:])] + [1]
```

<br>

---

### work with primes

<br>

```python
import math
import random


def find_greatest_common_divider(a, b) -> int:
    
    while(b != 0):
        result = b
        a, b = b, a % b
        
    return result


def _is_prime(number) -> bool:

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    
    return True


def find_prime_factors(number) -> list:
    
    divisors = [d for d in range(2, number//2 + 1) if number % d == 0]
    primes = [d for d in divisors if _is_prime(d)]

    return primes
```
