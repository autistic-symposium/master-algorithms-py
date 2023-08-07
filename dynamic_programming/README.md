## dynamic programming

<br>

* dynamic programming is the process of taking a recursive algorithm and cache overlapping problems (repeated calls). the runtime is given by the number of calls.
  
* **top-down** (**memoization**): how can we divide the problem into sub-problems?
  
* **bottom-up** (**tabulation**): solve for a simple case, then figure out for more elements.


<br>

---

### recursion

<br>

* recursion is an approach to solving problems using a function that calls itself as a subroutine. every time the function calls itself, it reduces the problem into subproblems. the recursion calls continue until it reaches a point where the subproblem can be solved without further recursion.

* a recursive function should have the following properties so it does not result in an infinite loop:
   * one or more base cases (a terminating scenario that does not use recursion to produce an answer)
   * a set of rules, also known as a recurrence relation, that reduces all other cases towards the base case.

* there can be multiple places where the function may call itself. 

* any recursion problem can be solved iteratively and vice-versa.

* the **master theorem** is an advanced technique of asymptotic analysis (time complexity) for many of the recursion algorithms that follow the pattern of divide-and-conquer.

<br>


#### vizualing the stack

<br>

* to visualize how the stack operates during recursion calls, check the example below where we reverse a string:

<br>

```python
def reverse(s):
   if len(s) == 0:
      return s
   else:
      return reverse(s[1:]) + s[0]
```

<br>


#### tail recursion

<br>

* tail recursion is a recursion where the recursive call is the final instruction in the recursion function. and there should be only one recursive call in the function.

* tail recursion is exempted from the space overhead discussed above, ad it skips an entire chain of recursive calls returning and returns straight to the original caller (it does not need a call stack for all the recursive calls - instead of allocating new space on the stack, the system could simply reuse the space allocated earlier for this second recursion call).

* when stack overflows, tail recursion might help.

* some languages' compiler recognizes tail recursion pattern and optimizes their execution (e.g., C and C++, but not Java, Rust, or Python - although it's possible to implement ad-hoc).

<br>

```python
def sum_non_tail_recursion(ls):
    if len(ls) == 0:
        return 0
    
    # not a tail recursion because it does some computation after the recursive call returned
    return ls[0] + sum_non_tail_recursion(ls[1:])


def sum_tail_recursion(ls):

    def helper(ls, acc):
        if len(ls) == 0:
            return acc

        # this is a tail recursion because the final instruction is a recursive call
        return helper(ls[1:], ls[0] + acc)
    
    return helper(ls, 0)
```

<br>



---

### memoization

<br>

* memoization is an optimization technique that avoids recursion's duplicate calculations.

* it's primarily used to speed up code by storing the intermediate results in a cache so that it can be reused later.

* for example, a hash table can be used as a cache and should be passed along each subroutine call.

<br>

```python
function dp(dp_state, memo_dict):

    if dp_state is the base cases
        return things like 0 or null
    
    if dp_state in memo_dict
        return memo_dict[dp_state]

    calculate dp(dp_state) from dp(other_state)
    save dp_state and the result into memo_dict

function answerToProblem(input) 
    return dp(start_state, empty_memo_dict)
```

<br>

* classic examples where memoization can be used are fibonacci and the "climbing stairs" problem:

<br>

```python
def climb_stairs_memoization(n: int) -> int:
 
    memo = {}    

    def helper(n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = helper(n-1, memo) + helper(n-2, memo)
        return memo[n]
 
   return helper(n, memo)
```

<br>

----

### time complexity

<br>

* the time complexity of a recursion algorithm is the product of the number of recursion invocations and the time complexity of the calculation, `R*O(s)`.

* you can also look at the "execution tree", which is a tree that is used to denote the execution flow of a recursive function in particular. each node represents an invocation of the recursive function. therefore, the total number of nodes in the tree corresponds to the number of recursion calls during the execution.
   * the execution tree of a recursive function would form a n-ary tree, with as the number of times recursion appears in the recurrence relation (for example, fibonacci would be a binary tree).
   * in a full binary tree with n levels, the total number of nodes is `2**N - 1`, so `O(2**N)` would be the time complexity of the function.
   * with memoization, fibonacci becomes `O(1)*N = O(N)`.

<br>

----

### space complexity

<br>

* there are mainly two parts of the space consumption that one should see in a recursive algorithm:
   * **recursion related space**: refers to the memory cost that is incurred directly by the recursion, i.e. the stack to keep track of recursive function calls. in order to complete a recursive call, the system allocates some space in the stack to hold: the returning address of the function call, the parameters that are passed to the function call, the local variables within the function call. once the function call is done, the space is freed. for recursive algorithms, the function calls chain up successively until it reaches a base case, so the space used for each call is accumulated. overconsumption can cause stack overflow.
   * **non-recursive related space**: refers to the memory that is not directly related to recursion, which includes the space (normally in heap) that is allocated for global variables.
 
<br>


---

### backtracking

<br>

* backtracking is a general algorithm for finding solutions to some computation problems, which incrementally builds candidates to the solution and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot lead to a valid solution.

* you can imagine the procedure as the tree traversal.

<br>

```python
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    for next in list_of_candidates:

        if is_valid(next_candidate):
            place(next_candidate)
            backtrack(next_candidate)
            remove(next_candidate)
````

