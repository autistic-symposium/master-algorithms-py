# given a string, write a function to check if it's a permutation of palindromes


def is_permutation_of_palindromes(some_string):

    aux_dict = {}

    for c in some_string.strip():

        # note: you could use a Counter dict here
        if c in aux_dict.keys():
            aux_dict[c] -= 1
        else:
            aux_dict[c] = 1
        
    for v in aux_dict.values():

        if v != 0:
            return False
        else:
            return True



if __name__ == "__main__":

    string1 = "abba"   
    string2 = "ab f ab"
    string3 = "e f ba"

    assert(is_permutation_of_palindromes(string1) == True)
    assert(is_permutation_of_palindromes(string2) == True)
    assert(is_permutation_of_palindromes(string3) == False)
