## stacks 


<br>

* stacks are **last in, first out** (LIFO) abstract structures, where the newest element is first one to be removed from the structure.

* a stack support `push` and `pop` at `O(1)`, and they be implemented with arrays or singly linked list.
  
* stacks are useful in **depth-first search** algorithms, where you can push temp data as you recurse, and remove them from the (memory or data structure) stack as you backtrace.

* to keep `find_min()` at `O(1)`, you can keep track of "prior minimum" when pushing and poping:

<br>

```python
class Stack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        self.stack.append((val, self.min))
        if self.min is not None:
            self.min = min(self.min, val)
        else:
            self.min = val

    def pop(self) -> None:
        if self.stack:
            (val, prior_min) = self.stack.pop()
            self.min = prior_min
            return val
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def get_min(self) -> int:
        return self.min
  ```
