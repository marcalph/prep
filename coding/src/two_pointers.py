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


def remove_nth_last_node(head: LinkedListNode | None, n: int) -> LinkedListNode | None:
    left: LinkedListNode | None = head
    right: LinkedListNode | None = head
    for _ in range(n):
        right = right.next  # type: ignore[union-attr]
    if right is None:
        return left.next if left else None  # we remove the head
    while right.next is not None:
        left = left.next  # type: ignore[union-attr]
        right = right.next
    left.next = left.next.next  # type: ignore[union-attr]
    return head


if __name__ == "__main__":
    print("hello")
