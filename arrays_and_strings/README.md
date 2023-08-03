## arrays and strings

<br>

### comparing strings

<br>

* "==" can be used to compare two strings only if the language support operator overloading (like C++).

<br>

----

### two-pointer technique

<br>

* a typical scenario is when you want to iterate the array from two ends to the middle. 
* another secnario is when you need one slow-runner and one fast-runner at the same time (so that you can determine the movement strategy for both pointers).
* in any case, this technique is usually used when the array is sorted.

<br>

---

### two-dimensional arrays

<br>

* in some languages (like C++), 2d arrays are represented as 1d, so an array of `m * n` elements represents `array[i][j]` as `array[i * n + j]`.
* dynamic 2d arrays a nested dynamic array.


<br>

---

### examples in this dir

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
