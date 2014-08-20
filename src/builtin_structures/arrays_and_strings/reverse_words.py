#!/usr/bin/python3

# Mari von Steinkirch @ 2013
# mari.wahl9@gmail.com

# Bernardo Sulzbach (mafagafo) @ 2014
# 1449441@gmail.com


def reverse_words(string):
    """
    Reverse the order of the words in a sentence.
    :param string: the string which words wil lbe reversed.
    :return: the reversed string.
    """
    l1 = string.split(' ')
    l1.reverse()
    return ' '.join(l1)


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

if __name__ == '__main__':
    phrase = 'I love  Google,   Fedora  & Python!'
    print(reverse_words(phrase))
    print(reverse_words_brute(phrase))
