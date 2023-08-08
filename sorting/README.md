## sorting 

<br>

* **inversions** in a sequence is a pair of elements that are out of order with respect to the ordering relation. a sorting algorithm is a sequence of operations that reduces inversions to zero.
  
* a **topological sort** of a directed graph is a way of ordering the list of nodes such that if `(a, b)` is a edge of the graph, then `a` appears before `b`. this type of sorting does not work if a graph has cycles or is not directed.

* because of their efficiencies, you usually want to use either merge sort or quick sort (`O(N log (N)`).

* other type of sorting algorithms can be seen below and in this directory's source code:

<br>


<p align="center">
<img src="https://github.com/go-outside-labs/master-algorithms-py/assets/138340846/54ab4d2c-a8b7-4e5c-9e98-5d7d2e627007" width="60%" align="center" style="padding:1px;border:1px solid black;">
</p>

<br>

---

### merge sort

<br>

```python
def ms(array):

  if len(array) < 2:
      return array

  mid = len(array) // 2
  left = array[:mid]
  right = array[mid:]

  result, i, j = [], 0, 0

  while i < len(left) and j < len(right):

      if left[i] <= right[j]:
          result.append(left[i])
          i += 1
      else:
          result.append(right[j])
          j += 1

  if left[i:]:
      result.extend(left[i:])
  if right[j:]:
      result.extend(right[j:])

  return result
```
