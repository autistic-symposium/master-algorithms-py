## sets

<br>

### implementing an `O(1)` randomized set class

<br>

* let's think about a set structure where we would implement insert, delete, and get_random at O(1) time. this type of structure widely used in statistical algorithms such as markov chain monte carlo and metropolis-hastings algorithms, which needs sampling from a probability distribution when it's difficult to compute the distribution itself.
* candidates for O(1) average insert time are:
    * **hashmaps (or hashsets)**: we could have problems with get_random(), as its idea is to choose a random index and then to retrieve an element with that index. since there is no indexes in hashmaps, to get a true random value, one would have to convert hashmap keys in a list, which is linear time. the solution would build a list of keys aside and use this list to compute get_random in constant time.
    * **array lists**: we could have time with delete, since to delete a value at arbitrary index takes linear time. the solution would be always delete the last value (first swap the element to delete with the last one, then pop the last element out). for that, we need to compute an index of each element in constant time, and we need a hashmap that stores `element -> index`.
* we see that both ways need the same combination of data structures: a hashmap and an array.
 
  <br>

```python
import random

class RandomizedSet:

    def __init__(self):
        self.set = []
        self.dict = {}
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.set.append(val)
        self.dict[val] = len(self.set)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:
            last_element, idx = self.set[-1], self.dict[val]
            self.set[idx], self.dict[last_element] = last_element, idx
            self.set.pop()
            del self.dict[val]
            return True
        return False
        
    def get_random(self) -> int:
        return random.choice(self.set)
  ```
