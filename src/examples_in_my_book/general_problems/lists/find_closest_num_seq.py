#!/usr/bin/python3

# Mari von Steinkirch @ 2013
# mari.wahl9@gmail.com


def find_closest_num_seq_unsorted(sequence):
    """
    Find the closest two numbers in a sequence.
    If we do this without sorting first, the runtime will be O(n^2).
    :param sequence: a sequence of numbers.
    """
    assert len(sequence) > 1, "Sequence must have at least 2 elements."
    biggest_difference = float("inf")
    for x in sequence:
        for y in sequence:
            if x == y:
                continue
            difference = abs(x - y)
            if difference < biggest_difference:
                best_x, best_y, biggest_difference = x, y, difference
    return best_x, best_y


def find_closest_num_seq_sorted(sequence):
    """
    Find the closest two numbers in a sequence.
    However, if we sort first, we can achieve it with runtime O(n log n).
    :param sequence: a sequence of numbers.
    """
    assert len(sequence) > 1, "Sequence must have at least 2 elements."
    sequence.sort()
    print(sequence)
    biggest_difference = float("inf")
    for i in range(len(sequence) - 1):
        x, y = sequence[i], sequence[i + 1]
        if x == y:
            continue
        difference = abs(x - y)
        if difference < biggest_difference:
            best_x, best_y, biggest_difference = x, y, difference
    return best_x, best_y


def test_find_closest_num_seq(module_name='this module'):
    import random
    seq = [random.randrange(100) for i in range(20)]
    print(seq)
    print(find_closest_num_seq_sorted(seq))
    print(find_closest_num_seq_unsorted(seq))

    s = 'Tests in {name} have {con}.'
    print(s.format(name=module_name, con='passed'))


if __name__ == '__main__':
    test_find_closest_num_seq()
