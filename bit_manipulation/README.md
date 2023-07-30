## bit manipulation

<br>

### `playing_with_bits.py`

<br>


```python
> python3 playing_with_bits.py

Integer number: 144
Binary number: 10010000

Update bit: 0b10010100
Set bit: 0b10010100
Clear bit: 0b10000000

I: 144, I2: 90
B: 10010000, B2: 01011010
Count bits swapped: 4

Swap bit in place: (90, 144)
```


----

### bit manipulations

<br>

* the base is a carry counting system with fixed digital symbols and rules.
* to convert a decimal number to a base-X non-decimal, you need to convert the integer part and the fractional part separately.
  * to convert the integer part, integer divide it by X until it reaches 0, and record the remainder each time.
  * traversing the remainder in reverse order will give the representation in the base-X system.
  * example: 50/2 = 25, 50%2 = 0, 25/2 = 12, 25%2 =1, 12/2 = 6, 12%2 = 0, 6/2 - 3, 6%2 =0, 3/2 = 1, 3%2 =1, 1/2 = 0, 1%2 = 1 --> 110010
  * to convert a fractional part, multiply the fractional part of the decimal number by X until it becomes 0, and record the integer part each time.
  * example: 0.6875x2 = 1.375 with integer 1, 0.375x2 = 0.75 with integer 0, 0.75x2 = 1.5 with integer 1, 0.5x2 = 1, with integer 1 --> 0.1011

<br>

----

### binary in computers:

<br>

* a single binary digit has two possible values, and a k-digit binary number can take 2^k possible values
* 1-byte number (8 digits binary number) has 2^8 possible values
* in a 1-byte signed integer, when the highest bit is 0, the 1-byte number ranges from 0 to 127 (2^7 - 1), when the highest bit is 1, it ranges from -128 to -1 (i.e., -128 to 127, which is -2^7 to 2^7 -1) 
* the binary representation of a number in a computer is called its machine number. it's a signed number, and the highest bit of the machine number is the sign bit 0.
* inverse code: for non-negative numbers, it's the same, for negative numbers, you flip every bit of the original code, except the sign bit.
* complement code: is obtained from the inverse code, for non-negative numbers it's the same, for negative numbers it's obtained by adding 1 to the inverse code. for example, for -10, the original code is 10001010, the inverse code is 11110101, and the complement code is 11110110.
* introducing the inverse code solves the problem of subtraction errors, but the issue of dual representation of 0 remains.
* the complement code solves both the subtraction error and dual representation of the 0 problem (in complement code, there is no -0).

<br>

----

### bit operations

<br>

- there are 6 types of bit operations: AND, OR, XOR, negation, left, shif, and right shift (shift operations are further divided into the arithmetic shift and logical shift).
- OR and AND are symmetrical operations.
- XOR: when the corresponding bits of the two numbers are the same, the result is 1.
- negation is unary: just flips the bit.
- left shift operation, `<<`, all binary bits are shift to the left (the high bits are discarded, and the low bits are filled with 0). for left shift operations, arithmetic shift and logical shift are the same.
- right shift operation, `>>`, all binary bits are shift to the right (low bits are discarded). how the high bits get filled differs between arithmetic shift and logical shift:
 - when shifting right arithmetically, the high bits are filled with the highest bit
 - when shifting right logically, the high bits are filled with 0
 - for non-negative numbers, the arithmetic right shift and logical right shift are identical
 - for signed types, the right shift operation is an arithmetic right shift; for unsigned types, the right shift operation is a logical right shift.
 - for languages without unsigned data type, the arithmetic right shift is `>>` and the logical shift is `>>>`.

<br>

----
  
### relationship with multiplication/division

<br>

* left shift corresponds to multiplication: shifting a number to the left by k bits is equivalent to multiplying the number by 2^k.
   * when the multiplier is not an integer power of 2, the multiplier can be split into the sum of the integer power of two. for example, a x 6 is equivalent to (a << 2) + (a << 1).
   * be careful against overflow.
* arithmetic right-shift corresponds to the division: shifting a number to the right by k bits is equivalent to dividing the number by 2^k for non-negative numbers.
   * integer division is rounded to 0, and the right shift operation is rounded down, which is also rounded to 0.
   * for negative numbers, integer division is rounded to 0, while the right shift is rounded down -> so it's not equivalent to dividing a number by 2^k

<br>

-----

### properties of bitwise operations

<br>

* idempotent: example, a & a = a
* commutativity: a & b = b &a
* associativity: (a & b) & c = a * (b & c)
* distributive: (a & b} | c = (a | c) & (b | c)
* de morgan's law: ~(a & b) = (~a) | (~b); ~ (a | b) = (~a) & (~b)
* 0 XOR: a XOR 0 = a; a XOR a = 0
* a & (a - 1) changes the last 1 in the binary representation of a to 0
* a & (-a) (equivalent to a & (~(a - 1)) keeps only the last 1 of the binary representation of a and sets the remaining 1s to 0


<br>

----

### two's complement method:

<br>

1. start with the equivalent positive number
2. invert (or flip) all bits, changing every 0 to 1, and every 1 to 0
3. add 1 to the entire inverted number, ignoring overflow

<br>

----

### hexadecimal

<br>

* an integer of type int can be represented as a 32-bit binary number.
* since a one-digit hexadecimal number corresponds to a four-digit binary number, an integer of type int can also be represented as an 8-bit hexadecimal number.


