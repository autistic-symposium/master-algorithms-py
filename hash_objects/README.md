## hash objects


<br>

* hash tables are data structure that organizes data using hash functions, in order to support quick insertion and search (map keys to buckets).
* ideally, a perfect hash function will be a 1-1 mapping between the key and the buckets. however, in most cases, a hash function is not perfect and there is a tradeoff between the amount of buckets and the capacity of a bucket.
* if the hash function is not a 1-1 mapping, collisions must be handled:
    - how to organize the values in the same bucket?
    - what if too many values are assigned to the same bucket?
    - how to search for a target value in a specific bucket?

<br>


<p align="center">
<img src="https://github.com/go-outside-labs/master-python-with-algorithms-py/assets/138340846/aa798e45-d53b-45b9-9f95-0e508eb923d7" width="60%" align="center" style="padding:1px;border:1px solid black;">
</p>



<br>

----

### notes on keys

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

* to implement a HashSet data structure, you need to implement:
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

----

### buckets as linked lists

<br>

* a good choice for buckets is linked lists, as their time complexity for insertion and deletion is constant (once the position to be updated is located). you just need to be sure you never insert repeated elements.
* time complexity for search is O(N/K) where N is the number of all possible values and K is the number of predefined buckets (the average size of bucket is N/K). 
* space complexity is O(K+M), where K is the number of predefined buckets, and M is the number of unique values that have been inserted in the HashSet. 
* lastly, to optimize search, we could maintain the buckets as sorted lists (and obtain O(logN) time complexity for the lookup operation). however, insert and delete are linear time (as elements would need to be shifted).

<br>

---

### buckets as binary search trees

<br>

* another option for a bucket is a binary search tree, with O(logN) time complexity for search, insert, and delete. in addition, bst can not hold repeated elements, just like sets.
* time complexity for search is O(logN/K), where N is the number of all possible values and K is the number of predefined buckets.
* space complexity is O(K+M) where K is the number of predefined buckets, and M is the number of unique values in the HashSet.

<br>

----

### implementing a hash map

<br>

* same as before, we need to tackle two main issues: hash function design and collision handling.
* a good approach is using a module function with an array or linked list. at this time, there is no constraint for repeated numbers.


<br>

