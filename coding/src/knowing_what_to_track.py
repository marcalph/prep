from collections import Counter

def permute_palindrome(st):
    cnt = Counter(st)
    # Replace this placeholder return statement with your code
    return len([v for v in cnt.values() if v%2==1]) <=1
