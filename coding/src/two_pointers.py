"""
The two-pointer technique is suitable when:

1. The input data can be traversed linearly, i.e., it's in an array, linked list, or a string of characters.
2. The focus is limited to a specific range of elements within the input data, as dictated by the positions of the two pointers, allowing us to consider a small subset of elements rather than the entire set.
3. Problems usually involve comparing or swapping values pointed to by two indexes. In less common cases, each index may move along a separate array or string.

However, the two-pointer technique is not suitable when:

1. The input data cannot be traversed linearly, i.e., it's not in an array, linked list, or a string of characters.
2. The problem requires an exhaustive search of the solution space, i.e., eliminating one solution does not eliminate any others.
"""

from coding.src.ll import LinkedList
from coding.src.ll_node import LinkedListNode


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


def remove_nth_last_node(head: LinkedListNode, n: int):
    left, right = head, head
    for _ in range(n):
        right = right.next
    if right is None:
        return left.next  # we remove the head
    while right.next is not None:
        left = left.next
        right = right.next
    left.next = left.next.next
    return head


if __name__ == "__main__":
    print("hello")
