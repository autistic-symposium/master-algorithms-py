## searching

<br>


### binary search

<br>

* a binary search operates on a contiguous sequence with a specified left and right index. this is called the search space.
* binary searching is composed of 3 sections:
    * pre-processing: sort if collection is unsorted
    * binary search: using a loop or recursion to divide search sapce in half after each comparison
    * post-processing: determine viable candidates in the remaining space

* there are 3 "templates" when writing a binary search:
    * `while left < right`, with `left = mid + 1` and `right = mid - 1`
    * `while left < right`, with `left = mid + 1` and `right = mid`, and `left` is returned
    * `while left + 1 < right`, with `left = 1` and `right = mid`, and `left` and `right` are returned
