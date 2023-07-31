## dynamic programming

<br>

* dynamic programming is the process of taking a recursive algorithm and cache overlapping problems (repeated calls).
* the runtime is given by the number of calls.
* **top-down**: how can we divide the problem into sub-problems?
    * top-down dynamic programming is called **memoization**.
* **bottom-up**: solve for a simple case, then figure out for more elements.

<br>

---

### recursion

<br>

* recursion is an approach to solving problems using a function that calls itself as a subroutine. every time the function calls itself, it reduces the problem into subproblems. the recursion calls continue until it reaches a point where the subproblem can be solved without further recursion.
* a recursive function should have the following properties so it does not result in an infinite loop:
   * one or more base cases (a terminating scenario that does not use recursion to produce an answer)
   * a set of rules, also known as recurrence relation, that reduces all other cases towards the base case.
* there can be multiple places where the function may call itself. 
* any recursion problem can be solved iteratively and vice-versa.

<br>

#### vizualing the stack

<br>

* to visualize how the stack operates during recursion calls, check the example below where we reverse a string:

```python
def reverse(s):
   if len(s) == 0:
      return s
   else:
      return reverse(s[1:]) + s[0]
```

<br>

---

### memoization

<br>

* memoization is an optimization technique that avoids recursion's duplicate calculations.
* it's primarily used to speed up code by storing the intermediate results in a cache so that it can be reused later.
* for example, a hash table can be used as a cache and should be passed along each subroutine call.
* classical examples are fibonnaci and the "climbing stairs" problem:

```python
cache = {1: 1, 0: 1}
    
def climbing_stairs(n) -> int:
        
   if n not in cache:
         cache[n] = climbing_stairs(n-1) + climbing_stairs(n-2)
        
   return cache[n]
```



