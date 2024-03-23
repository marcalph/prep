# Two pointers is useful when we want to find 2 elements that verify a condiiton in a array traversed linearly
# it is not adapted when we don't traverse linearly (i.e.) or need an exhaustive search
def is_palindrome(s: str):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


def sum_of_three(arr: list[int], target):
    arr.sort()
    for idx in range(len(arr) - 2):
        val = arr[idx]
        lo, hi = idx + 1, len(arr) - 1
        while lo < hi:
            current_sum = val + arr[lo] + arr[hi]
            if current_sum < target:
                lo += 1
            elif current_sum > target:
                hi -= 1
            else:
                return True
    return False


if __name__ == "__main__":
    print("hello")
