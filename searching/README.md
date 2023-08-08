## binary search

<br>

* a binary search operates on a (sorted) contiguous sequence with a specified left and right index (this is called the **search space**).
  
* binary searching is composed of 3 sections:
    * **pre-processing**: sort if collection is unsorted
    * **binary search**: using a loop or recursion to divide search space in half after each comparison (`O(log(N)`)
    * **post-processing**: determine viable candidates in the remaining space

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
    
    if item == array[mid]:
        return mid
        
    elif item < array[mid]:
        return binary_search_recursive(array, item, mid - 1, lower)
        
    else:
        return binary_search_recursive(array, item, higher, mid + 1)
```

<br>

* or a slightly different version that does not carry `lower` and `higher`:

<br>

```python
def binary_search_recursive(array, item):

    start, end = 0, len(array)
    mid = (end - start) // 2

    while len(array) > 0:
        if array[mid] == item:
            return True
        elif array[mid] > item:
            return binary_search_recursive(array[mid + 1:], item)
        else:
            return binary_search_recursive(array[:mid], item)
    
    return False
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

<br>

---

### find min in a rotated array

<br>

```python
def find_min(nums):
        
        left, right = 0, len(nums) - 1
        
        while nums[left] > nums[right]:
            
            mid = (left + right) // 2
            
            if nums[mid] < nums[right]:
                right = mid
            else:
                left =  mid + 1
                
        return nums[left]
```

<br>

---

### find a peak element

<br>

* a peak element is an element that is strictly greater than its neighbors.

<br>

```python
def peak_element(nums):

        left, right = 0, len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid + 1] < nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left
```

<br>

---

### find a desired sum

<br>

* if the array is sorted:

<br>

```python
def find_pairs_max_sum(array, desired_sum):

    i, j = 0, len(array) - 1

    while i < j:
        this_sum = array[i] + array[j]
        if this_sum == desired_sum:
            return array[i], array[j]
        elif this_sum > desired_sum:
            j -= 1
        else:
            i += 1
            
    return False
```

<br>

* if the array is not sorted, use a hash table:

<br>

```python
def find_pairs_not_sorted(array, desired_sum):

    lookup = {}

    for item in array:
        key = desired_sum - item

        if key in lookup.keys():
            lookup[key] += 1
        else:
            lookup[key] = 1

    for item in array:
        key = desired_sum - item

        if item in lookup.keys():
            if lookup[item] == 1: 
                return (item, key)
            else:
                lookup[item] -= 1

    return False
```
