## arrays, strings, hash objects

<br>

### hash objects

<br>

* hash tables are data structure that organizes data using hash functions, in order to support quick insertion and search (map keys to buckets).
* ideally, a perfect hash function will be a 1-1 mapping between the key and the buckets. however, in most cases, a hash function is not perfect and there is a tradeoff between the amount of buckets and the capacity of a bucket.
* if the hash function is not a 1-1 mapping, collisions must be handled:
    - how to organize the values in the same bucket?
    - what if too many values are assigned to the same bucket?
    - how to search for a target value in a specific bucket?

<br>
<img width="732" src="https://github.com/go-outside-labs/master-python-with-algorithms-py/assets/138340846/aa798e45-d53b-45b9-9f95-0e508eb923d7">

<br>
<br>

#### implementing a hash set

<br>

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

#### buckets as linked lists

<br>

* a good choice for buckets is linked lists, as their time complexity for insertion and deletion is constant (once the position to be updated is located). 
* time complexicity for search is O(N/K) where N is the number of all possible values and K is the number of predefined buckets (the average size of bucket is N/K). 
* space complexity is O(K+M), where K is the number of predefined buckets, and M is the number of unique values that have been inserted in the HashSet. 
* lastly, to optimize search, we could maintain the buckets as sorted lists (and obtain O(logN) time complexity for the lookup operation). however, insert and delete are linear time (as elements would need to be shifted).

<br>

#### buckets as binary search trees

<br>

* another option for a bucket is a binary search tree, with O(logN) time complexity for search, insert, and delete.
* time complexity for search is O(logN/K), where N is the number of all possible values and K is the number of predefined buckets.
* space complexity is O(K+M) where K is the number of predefined buckets, and M is the number of unique values in the HashSet.

<br>

---

### examples

<br>

#### `is_palindrome.py`

<br>

```python
python3 is_palindrome.py

Testing is_palindrome()...
Is subi no onibus a palindrone?: True
Is helllo there a palindrone?: False
```

<br>

#### `playing_with_strings.py`

<br>

```python
python3 playing_with_strings.py

Testing reverse_array_in_place
Array: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
```

<br>

#### `anagram.py`

<br>

```python
python3 anagram.py

Testing is_anagram()...
Is listen an anagram of silent?: True
```

<br>

#### `permutation.py`

<br>

```python
python3 permutation.py

Testing permutation()...
Permutation of bt3gl: ['bt3gl', 'bt3lg', 'btg3l', 'btgl3', 'btl3g', 'btlg3', 'b3tgl', 'b3tlg', 'b3gtl', 'b3glt', 'b3ltg', 'b3lgt', 'bgt3l', 'bgtl3', 'bg3tl', 'bg3lt', 'bglt3', 'bgl3t', 'blt3g', 'bltg3', 'bl3tg', 'bl3gt', 'blgt3', 'blg3t', 'tb3gl', 'tb3lg', 'tbg3l', 'tbgl3', 'tbl3g', 'tblg3', 't3bgl', 't3blg', 't3gbl', 't3glb', 't3lbg', 't3lgb', 'tgb3l', 'tgbl3', 'tg3bl', 'tg3lb', 'tglb3', 'tgl3b', 'tlb3g', 'tlbg3', 'tl3bg', 'tl3gb', 'tlgb3', 'tlg3b', '3btgl', '3btlg', '3bgtl', '3bglt', '3bltg', '3blgt', '3tbgl', '3tblg', '3tgbl', '3tglb', '3tlbg', '3tlgb', '3gbtl', '3gblt', '3gtbl', '3gtlb', '3glbt', '3gltb', '3lbtg', '3lbgt', '3ltbg', '3ltgb', '3lgbt', '3lgtb', 'gbt3l', 'gbtl3', 'gb3tl', 'gb3lt', 'gblt3', 'gbl3t', 'gtb3l', 'gtbl3', 'gt3bl', 'gt3lb', 'gtlb3', 'gtl3b', 'g3btl', 'g3blt', 'g3tbl', 'g3tlb', 'g3lbt', 'g3ltb', 'glbt3', 'glb3t', 'gltb3', 'glt3b', 'gl3bt', 'gl3tb', 'lbt3g', 'lbtg3', 'lb3tg', 'lb3gt', 'lbgt3', 'lbg3t', 'ltb3g', 'ltbg3', 'lt3bg', 'lt3gb', 'ltgb3', 'ltg3b', 'l3btg', 'l3bgt', 'l3tbg', 'l3tgb', 'l3gbt', 'l3gtb', 'lgbt3', 'lgb3t', 'lgtb3', 'lgt3b', 'lg3bt', 'lg3tb']
```
