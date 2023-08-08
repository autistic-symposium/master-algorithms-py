## binary search

<br>

* a binary search operates on a contiguous sequence with a specified left and right index (this is called the **search space**).
  
* binary searching is composed of 3 sections:
    * **pre-processing**: sort if collection is unsorted
    * **binary search**: using a loop or recursion to divide search space in half after each comparison (`O(log(N)`)
    * **post-processing`: determine viable candidates in the remaining space

* there are 3 "templates" when writing a binary search:
    * `while left < right`, with `left = mid + 1` and `right = mid - 1`
    * `while left < right`, with `left = mid + 1` and `right = mid`, and `left` is returned
    * `while left + 1 < right`, with `left = mid` and `right = mid`, and `left` and `right` are returned


<br>

----

### iterative

<br>

```python
    if lens(nums) == 0:
        return False
        
    lower, higher = 0, len(array)

    while lower < higher:
        mid = (higher + lower) // 2
        
        if array[mid] == item:
            return mid 
        elif array[mid] > item:
            higher = mid - 1
        else:
            lower = mid + 1
            
    return False
```

<br>

----

### recursive

<br>

```python
def binary_search_recursive(array, item, higher=None, lower=0):

    higher = higher or len(array)
    
    if higher < lower:
        return False
    
    mid = (higher + lower) // 2
    
    if  item == array[mid]:
        return mid
        
    elif item < array[mid]:
        return binary_search_recursive(array, item, mid - 1, lower)
        
    else:
        return binary_search_recursive(array, item, higher, mid + 1)
```

<br>

---

### in a matrix

<br>

```python
def binary_search_matrix(matrix, item, lower=0, higher=None):

    if not matrix:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    higher = higher or rows * cols

    if higher > lower:
        mid = (higher + lower) // 2
        row = mid // cols
        col = mid % cols

        if item == matrix[row][col]:
            return row, col
        elif item < matrix[row][col]:
            return binary_search_matrix(matrix, item, lower, mid - 1)
        else:
            return binary_search_matrix(matrix, item, mid + 1, higher)
        
    return False
```

<br>

---

### find the square root

<br>

```python

def sqrt(x) -> int:
    
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            
            mid = (right + left) // 2
            num = mid * mid
            
            if num > x:
                right = mid - 1
                
            elif num < x:
                left = mid + 1
                
            else:
                return mid
            
        return right
```
