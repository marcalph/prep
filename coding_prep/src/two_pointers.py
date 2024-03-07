# Two poitners useful when we want to find 2 elements that verify a condiiton in a array traversed linearly
# it is not adapted when we can't traverse linearly (i.e.) or need an exhaustive search
def is_palindrome(s: str):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


if __name__ == "__main__":
    print("hello")
