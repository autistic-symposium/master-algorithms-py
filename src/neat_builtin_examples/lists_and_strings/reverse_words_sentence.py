
#!/usr/bin/env python

author = "Mari Wahl"
email = "marina.w4hl@gmail.com"

""" Here we want to invert the words in a string, without reverting
the words.

Important things to remember:

1. python strings are immutable
2. The last word doesn't not end by a space, so we need to make
sure we get the last word too

The solution consists of two loops,
1) revert all the characters with 2 pointers
2) search for spaces and revert the words, two pointers too
3) You can represent space as ' ' or as u'\u0020'
4) Do we want to look to ! ; , . etc?

In the solutions bellow, we show how to do this logic, and how to use
python's methods to do in a few lines
"""


# EXAMPLE NUMBER 1

def reverser(string1, p1=0, p2=None):
    if len(string1) < 2:
        return string1
    p2 = p2 or len(string1)-1
    while p1 < p2:
        aux = string1[p1]
        string1[p1] = string1[p2]
        string1[p2] = aux
        p1 += 1
        p2 -= 1



def reversing_words_setence_logic(string1):
    reverser(string1)
    p = 0
    start = 0
    final = []
    while p < len(string1):
        if string1[p] == u"\u0020":
            reverser(string1,start,p-1)
            start = p+1
        p += 1
    reverser(string1,start,p-1)

    return "".join(string1)



# EXAMPLE NUMBER 2 AND 3 USING PYTHON AWESOMESAUCE

def reversing_words_setence_py(str1):
    ''' reverse the words in a sentence'''
    words = str1.split()
    rev_set = " ".join(reversed(words))
    return rev_set

def reversing_words_setence_py2(str1):
    """
    Reverse the order of the words in a sentence.
    :param string: the string which words wilL be reversed.
    :return: the reversed string.
    """
    words = str1.split(' ')
    words.reverse()
    return ' '.join(words)


# EXAMPLE 4, VERY SILLY, USING BRUTE FORCE
#
def reverse_words_brute(string):
    """
    Reverse the order of the words in a sentence.
    :param string: the string which words wil lbe reversed.
    :return: the reversed string.
    """
    word, sentence = [], []
    for character in string:
        if character != ' ':
            word.append(character)
        else:
            # So we do not keep multiple whitespaces. An empty list evaluates to False.
            if word:
                sentence.append(''.join(word))
            word = []
    # So we do not keep multiple whitespaces. An empty list evaluates to False.
    if word != '':
        sentence.append(''.join(word))
    sentence.reverse()
    return ' '.join(sentence)



# TESTS

def test_reversing_words_sentence():
    str1 = "Buffy is a Vampire Slayer"
    assert(reversing_words_setence_py(str1) == "Slayer Vampire a is Buffy")
    assert(reversing_words_setence_py2(str1) == "Slayer Vampire a is Buffy")
    assert(reverse_words_brute(str1) == "Slayer Vampire a is Buffy")
    assert(reversing_words_setence_logic(list(str1)) == "Slayer Vampire a is Buffy")

    print("Tests passed!")



if __name__ == '__main__':
    test_reversing_words_sentence()


