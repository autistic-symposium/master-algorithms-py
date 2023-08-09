## sets

<br>


### implementing an `O(1)` randomized set class

<br>

* a set structure where we would implement `insert`, `delete`, and `get_random` at `O(1)` time.

* this type of structure is widely used in statistical algorithms such as markov chain monte carlo and metropolis-hastings algorithms, which needs sampling from a probability distribution when it's difficult to compute the distribution itself.
  
* candidates for `O(1)` average insert time are:
    * **hashmaps (or hashsets)**: to be able to implement `get_random` at `O(1)` (choose a random index and retrieve a random element), we would have to convert hashmap keys in a list, which is `O(N)`. a solution is to build a list of keys aside and use this list to compute `get_random` in `O(1)`.
    * **array lists**: we would have `O(N)` with `delete`. the solution would be delete the last value (first swap the element to delete with the last one, then pop the last element out). for that, we need to compute an index of each element in `O(N)`, and we need a hashmap that stores `element -> index`.

* either way, we need the same combination of data structures: a hashmap and an array.
   * an array keeps the values appended in order. `delete` always replace elements to the end.
   * an dictionary maps the values (key) to the corresponding length of the array (their index) so it guarantees `O(1)` lookup and provides a list for `random.choice()`. 
 
  <br>

```python
import random

class RandomizedSet:

    def __init__(self):
        self.random_set = {}
        self.index_list = []
        
    def insert(self, val: int) -> bool:
        
        if val in self.random_set.keys():
            return False
            
        self.index_list.append(val)
        self.random_set[val] = len(self.index_list)
        
        return True

    def remove(self, val: int) -> bool:
        
        if val in self.random_set.keys():
            
            last_element = self.index_list[-1]
            index_val = self.random_set[val]
            self.index_list[index_val] = last_element
            self.random_set[last_element] = index_val
            
            self.index_list.pop()
            del self.random_set[val]
            
            return True
            
        return False
        
    def get_random(self) -> int:
        return random.choice(self.index_list)
  ```
