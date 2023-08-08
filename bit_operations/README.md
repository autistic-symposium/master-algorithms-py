## bit manipulation


<br>

### techniques

<br>

* test if kth bit is set: `num & (1 << k) != 0`

* set kth bit: `num |= (1 << k)`

* turn off kth bit: `num &= ~(1 << k)`

* toggle the kth bit: `num ^= (1 << k)`

* multiply by `2^k`: `num << k`

* dvide by `2^k`: `num >> k`

* check if a number is a power of 2: `(num & num - 1) == 0` or `(num & (-num)) == num`

* swapping two variables: `num1 ^= num2; num2 ^= num`; `num1 ^= num2`



<br>

---

### converting a decimal to another base (`X`)

<br>

* the **base** is a carry counting system with fixed digital symbols and rules.

* you need to convert the integer part and the fractional part separately.

* to convert the integer part, integer divide it by `X` until it reaches `0`, and record the remainder each time.

* traversing the remainder in reverse order will give the representation in the base-X system.

```
50/2 = 25, 25/2 = 12, 12/2 = 6, 6/2 = 3,  3/2 = 1, 1/2 = 0
50%2 = 0, 25%2 = 1, 12%2 = 0, 6%2 = 0, 3%2 = 1, 1%2 = 1 
--> 110010
```

* to convert a fractional part, multiply the fractional part of the decimal number by `X `until it becomes `0`, and record the integer part each time.

```
0.6875x2 = 1.375 with integer 1,
0.375x2 = 0.75 with integer 0,
0.75x2 = 1.5 with integer 1,
0.5x2 = 1, with integer 1
--> 0.1011
```

<br>

```python
def convert_to_any_base(base: int, num: int) -> str:
        
        if num == 0:
            return "0"
    
        n = abs(num)
        result = ""
        
        while n:
            result += str(n % base)
            n //= base
        
        if num < 0: 
            result += '-'
            
        return  result[::-1]
```

<br>



----

### hexadecimal

<br>

* an integer of type int can be represented as a `32-bit` binary number.
  
* since a one-digit hexadecimal number corresponds to a four-digit binary number, an integer of type int can also be represented as an `8-bit` hexadecimal number.

<br>

```python
def convert_to_hex(num: int) -> str:
      
  hex_chars  = "0123456789abcdef"
  size = 32
  base = 16
        
  if num == 0:
    return "0"
        
  if num < 1:
    num += 2**size
        
  result = ""
  while num:
    result += hex_chars[num % base]
    num //= base
            
  return result[::-1]
```

<br>

----

### binary in computers

<br>

* a single binary digit has two possible values, and a `k`-digit binary number can take `2^k` possible values.
  
* `1-byte` number (`8` digits binary number) has `2^8` possible values.
  
* in a `1-byte` signed integer, when the highest bit is `0`, the `1-byte` number ranges from `0` to `127` (`2^7 - 1`), when the highest bit is `1`, it ranges from `-128` to `-1` (*i.e.,* `-128` to `127`, which is `-2^7` to `2^7 -1`).
  
* the binary representation of a number in a computer is called its **machine number**. it's a signed number, and the highest bit of the machine number is the sign bit `0`.
  
* inverse code: for non-negative numbers, it's the same, for negative numbers, you flip every bit of the original code, except the sign bit.
        * introducing the inverse code solves the problem of subtraction errors, but the issue of dual representation of `0` remains.
* complement code: is obtained from the inverse code, for non-negative numbers it's the same, for negative numbers it's obtained by adding `1` to the inverse code. for example, for `-10`, the original code is `10001010`, the inverse code is `11110101`, and the complement code is `11110110`.
        * the complement code solves both the subtraction error and dual representation of the `0` problem (in complement code, there is no `-0`).,

<br>

----

### bit operations

<br>

- there are 6 types of bit operations: `AND`, `OR`, `XOR`, `negation`, `left shift`, and `right shift` (shift operations are further divided into the arithmetic shift and logical shift):
   - `OR` and `AND`: symmetrical operations.
   - `XOR`: when the corresponding bits of the two numbers are the same, the result is `1`.
   - negation is unary: just flips the bit.
   - left shift operation, `<<`, all binary bits are shift to the left (the high bits are discarded, and the low bits are filled with 0). for left shift operations, arithmetic shift and logical shift are the same.
   - right shift operation, `>>`, all binary bits are shift to the right (low bits are discarded). how the high bits get filled differs between arithmetic shift and logical shift:
  - when shifting right arithmetically, the high bits are filled with the highest bit.
  - when shifting right logically, the high bits are filled with `0`.
  - for non-negative numbers, the arithmetic right shift and logical right shift are identical.
  - for signed types, the right shift operation is an arithmetic right shift; for unsigned types, the right shift operation is a logical right shift.
  - for languages without unsigned data type, the arithmetic right shift is `>>` and the logical shift is `>>>`.

<br>

----
  
### relationship with multiplication/division

<br>

* left shift corresponds to multiplication: shifting a number to the left by `k` bits is equivalent to multiplying the number by `2^k`.
   * when the multiplier is not an integer power of `2`, the multiplier can be split into the sum of the integer power of two.
   * for example, `a x 6` is equivalent to `(a << 2) + (a << 1)`.
   * be careful against overflow.
     
* arithmetic right-shift corresponds to the division: shifting a number to the right by k bits is equivalent to dividing the number by `2^k` for non-negative numbers.
   * integer division is rounded to `0`, and the right shift operation is rounded down, which is also rounded to `0`.
   * for negative numbers, integer division is rounded to `0`, while the right shift is rounded down -> so it's not equivalent to dividing a number by `2^k`.

<br>

-----

### properties of bitwise operations

<br>

* idempotent: `a & a = a`
  
* commutativity: `a & b = b &a`
  
* associativity: `(a & b) & c = a * (b & c)`
  
* distributive: `(a & b} | c = (a | c) & (b | c)`
  
* de morgan's law: `~(a & b) = (~a) | (~b); ~ (a | b) = (~a) & (~b)`
  
* 0 XOR: `a XOR 0 = a`; `a XOR a = 0`
  
* `a & (a - 1)` changes the last 1 in the binary representation of a to 0.
  
* ` a & (-a)` (equivalent to `a & (~(a - 1)`) keeps only the last 1 of the binary representation of a and sets the remaining 1s to 0.


<br>

----

### two's complement method

<br>

* the complement is the number with respect to `2**n`:

1. start with the equivalent positive number
2. invert (or flip) all bits, changing every `0` to `1`, and every `1` to `0`
3. add `1` to the entire inverted number, ignoring overflow

<br>

---

### playing with bits

<br>

```python
def count_ones(n: int) -> int:
        
        counter = 0
        
        while n:
            
            if n & 1:
                counter += 1
            
            n >>= 1
        
        return counter

def set_bit(num, i):
    mask = 1 << i
    return bin( num | mask )

def update_bit(num, i, v):
    mask = ~ (1 << i)
    return bin( (num & mask) | (v << i) )

def count_bits_swapped(a, b):
    count = 0
    m = a^b
    while m:
        count +=1
        m = m & (m-1)
    return count

def clear_bit(num, i):
    mask = ~ (1 << i)   # -0b10001
    return bin(num & mask)

def swap_bit_in_place(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a, b

def find_how_many_1_in_a_binary(num):

    counter = 0
    while num:
        if num & 1:
            counter += 1
        num >>= 1
    return counter

def reverse_bits(n: int) -> int:
        
        result, base = 0, 31
        while n:
            result += (n & 1) << base
            n >>= 1
            base -= 1
        
        return result

def get_sum(self, a: int, b: int) -> int:
        
       if a == -b:
            return 0
        
       if abs(a) > abs(b):
            a, b = b, a
            
       if a < 0:
            return - get_sum(-a, -b)
        
       while b:
            
            c = a & b
            a, b = a ^ b, c << 1
            
       return a
```
