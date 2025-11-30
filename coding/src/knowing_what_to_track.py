"""
Use this under the following conditions:
    Frequency Tracking: The problem involves tallying the occurrences of individual elements or combinations of elements within a dataset.
    Pattern Recognition: The problem involves identifying recurring patterns or frequent repetitions of certain elements or combinations in the dataset, whihc points to freq counting.

    Limited Output Options: The problem's solution involves selecting from a limited set of possible outputs, such as Yes/No, True/False, Valid/Invalid, Player 1/Player 2.
"""

from collections import Counter

from collections import Counter


def permute_palindrome(st):
    """
    Check if a given string can be rearranged to form a palindrome.
    """
    cnt = Counter(st)
    return len([v for v in cnt.values() if v % 2 == 1]) <= 1


def is_anagram(str1, str2):
    """
    Check if two strings are anagrams of each other.
    """
    if len(str1) != len(str2):
        return False

    hm = {}
    for ch in str1:
        hm[ch] = hm.get(ch, 0) + 1
    for ch in str2:
        hm[ch] = hm.get(ch, 0) - 1
    vals = hm.values()
    return len(list(filter(lambda x: x != 0, vals))) == 0


class FreqStack:
    """
    A class representing a frequency stack.
        push(value): Pushes the given value into the stack.
        pop(): Pops and returns the most frequent element from the stack.
    """

    def __init__(self):
        self.inp = []
        self.hm = {}

    def push(self, value):
        self.inp.append(value)
        self.hm[value] = self.hm.get(value, 0) + 1

    def pop(self):
        maxfreq = 0
        for freq in self.hm.values():
            if freq > maxfreq:
                maxfreq = freq

        for i, j in enumerate(self.inp[::-1]):
            if maxfreq == self.hm[j]:
                self.inp.pop(-(i + 1))
                self.hm[j] -= 1
                break
        return j
