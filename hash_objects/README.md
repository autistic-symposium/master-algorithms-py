## hash objects


<br>

* hash tables (also known as hash maps) are data structure that organizes data using hash functions, in order to support quick insertion and search (map keys to buckets).

<br>



<p align="center">
<img src="https://github.com/go-outside-labs/master-python-with-algorithms-py/assets/138340846/aa798e45-d53b-45b9-9f95-0e508eb923d7" width="60%" align="center" style="padding:1px;border:1px solid black;">
</p>


<br>

---

### collision

<br>

* ideally, a perfect hash function will be a 1-1 mapping between the key and the buckets. however, in most cases, a hash function is not perfect and there is a tradeoff between the amount of buckets and the capacity of a bucket. if the hash function is not a 1-1 mapping, collisions must be handled:
    - how to organize the values in the same bucket?
    - what if too many values are assigned to the same bucket?
    - how to search for a target value in a specific bucket?

* popular collision techniques are:
    - separate chaining: a linked list is used for each value, so that it stores all the collided items.
    - open addressing: all entry records are stored in the bucket array itself. when a new entry has to be inserted, the buckets are examined, starting with the hashed-to slot and proceeding in some probe sequence, until an unoccupied slot is found. 


<br>

----

### keys

<br>

* when the order of each element in the string/array doesn't matter, you can use the sorted string/array as the key.
* if you only care about the offset of each value, you can use it as as the key.
* in a tree, you might want to directly use the `Node()` class as key sometimes, but in general, the serialization of the subtree might be a better idea.
* in a matrix, you might want to use the row index or the column index as key. sometimes you might want to aggregate the values in the same diagonal line.

<br>

---

### implementing a hash set

<br>

* the difference between a hash set and a hash map is that the set can never have repeated elements.

* to implement a hash set data structure, you need to implement:
    - a hash function (to assign an address to store a given value), and
    - a collision handling (since the nature of a hash function is to map a value from a space A to a corresponding smaller space B).

    
* overall, there are several strategies to resolve the collisions:
    - separate chaining: for value with the same hash key, we keep them in a bucket, and each bucket is independent of each other.
    - open addressing: whenever there is a collision, we keep on probing the main space with certain strategy until a free slot is found.
    - 2-choices hashing: we use two hash functions rather than one, and pick the generated address with fewer collisions.

    
* if we were to implement separate chaining, the primary storage underneath a hashset is a continuous memory as array, where each element in this array corresponds to a bucket that store the actual values.
    * given a value, first we generate a key for the value via the hash function (the generated key serves as the index to locate the bucket).
    * once the bucket is located, we then perform the desired operation on the bucket (such as add, remove, and contain).
    * use a prime number as the base of the module to reduce collisions.

<br>

```python
class HashSet:

    def __init__(self, size):
        self.size = size
        self.bucket = [Bucket() for _ in range(self.size)]

    def _get_hash_key(self, key):
        return key % self.size

    def add(self, element: int) -> None:
        bucket_index = self._get_hash_key(element)
        self.bucket[bucket_index].insert(element)
    
    def remove(self, element: int) -> None:
        bucket_index = self._get_hash_key(element)
        self.bucket[bucket_index].delete(element)

    def contains(self, element: int) -> bool:
        bucket_index = self._get_hash_key(element)
        return self.bucket[bucket_index].exists(element)
````

<br>


#### buckets as linked lists

<br>

* a good choice for buckets are linked lists, as their time complexity for insertion and deletion is constant (once the position to be updated is located). you just need to be sure you never insert repeated elements.
* time complexity for search is `O(N/K)` where `N` is the number of all possible values and `K` is the number of predefined buckets (the average size of bucket is `N/K`). 
* space complexity is `O(K+M)`, where `K` is the number of predefined buckets, and `M` is the number of unique values that have been inserted in the HashSet. 
* lastly, to optimize search, we could maintain the buckets as sorted lists (and obtain `O(log(N))` time complexity for the lookup operation). however, insert and delete are linear time (as elements would need to be shifted).

<br>

```python
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def insert(self, value):
        if not self.exists(value):
            self.head.next =  Node(value, self.head.next)
        else:
            print(f'node {value} already exists')
        
    def delete(self, value):
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def exists(self, value):
        current = self.head.next
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False
```


<br>

#### buckets as binary search trees

<br>

* another option for a bucket is a binary search tree, with `O(log(N))` time complexity for search, insert, and delete. in addition, bst can not hold repeated elements, just like sets.
* time complexity for search is `O(log (N/K)`, where `N` is the number of all possible values and `K` is the number of predefined buckets.
* space complexity is `O(K+M)` where `K` is the number of predefined buckets, and `M` is the number of unique values in the hash set.

<br>

```python        
class Node:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None


class Bucket:
    def __init__(self):
        self.tree = BSTree()

    def insert(self, value):
        self.tree.root = self.tree.insert(self.tree.root, value)
        
    def delete(self, value):
        self.tree.root = self.tree.delete(self.tree.root, value)
    
    def exists(self, value):
        return (self.tree.search(self.tree.root, value) is not None)


class BSTree():
    def __init__(self):
        self.root = None

    def search(self, root, value) -> Node:
        if root is None or value == root.val:
            return root

        return self.search(root.left, value) if val < root.value \
            else self.search(root.right, value)
    
    def insert(self, root, value) -> Node:
        if not root:
            return Node(value)
        
        if value > root.val:
            root.right = self.insert(root.right, value)
        elif value == root.val:
            return root
        else:
            root.left = self.insert(root.left, value)
    
    def successor(self, root):
        # one step right and then all left
        root = root.right
        while root.left:
            root = root.left
        return root.value
    
    def predecessor(self, root):
        # one step left and then always right
        root = root.left
        while root.right:
            root = root.right
        return root.value

    def delete(self, root, key) -> TreeNode:
        if not root:
            return None

        if key > root.val:
            root.right = self.delete(root.right, key)
        
        elif key < root.val:
            root.left = self.delete(root.left, key)
        
        else:
            if not (root.left or root.right):
                root = None
            elif root.right:
                root.val = self.sucessor(root)
                root.right = self.delete(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.delete(root.left, root.val)
        
        return root
```

<br>

----

### implementing a hash map

<br>

* same as before, we need to tackle two main issues: hash function design and collision handling.
* a good approach is using a module function with an array or linked list. at this time, there is no constraint for repeated numbers.

<br>

```python
class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def put(self, key, value):
        found = False
        for i, k in enumerate(self.bucket):
            if key == k[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for i, k in enumerate(self.bucket):
            if key == k[0]:
                # del is an O(N) operation, as we would copy all the i: elements
                # to make it O(1) we could swap the element we want to remove
                # with the last element in the bucket
                del self.bucket[i]
```
<br>

