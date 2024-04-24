"""
Use this under the following conditions:
    Frequency Tracking: The problem involves tallying the occurrences of individual elements or combinations of elements within a dataset.
    Pattern Recognition: The problem involves identifying recurring patterns or frequent repetitions of certain elements or combinations in the dataset, whihc points to freq counting.

    Limited Output Options: The problem's solution involves selecting from a limited set of possible outputs, such as Yes/No, True/False, Valid/Invalid, Player 1/Player 2.
"""
from collections import Counter

def permute_palindrome(st):
    cnt = Counter(st)
    # Replace this placeholder return statement with your code
    return len([v for v in cnt.values() if v%2==1]) <=1



def is_anagram(str1, str2):
    if len(str1) != len (str2):
    # Replace this placeholder return statement with your code
        return False

    hm = {} 
    for ch in str1:
        hm[ch] = hm.get(ch, 0) + 1
    for ch in str2:
        hm[ch] = hm.get(ch, 0) - 1
    vals = hm.values()
    return len(list(filter(lambda x:x!=0, vals)))==0 