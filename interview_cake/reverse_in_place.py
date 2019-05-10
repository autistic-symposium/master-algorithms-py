# Write a function that takes a list of characters and reverses the letters in place.
# O(n) time and O(1)O(1) space.

def reverse_in_place(char_list):
    return char_list[::-1]


char_list = ['a', 'b', 'c', 'd', 'e', 'f']



print(char_list)
print(reverse_in_place(char_list))