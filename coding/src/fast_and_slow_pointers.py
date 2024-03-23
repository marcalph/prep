"""
The fast and slow pointer technique is suitable when:
    1. The problem involves identifying:
        - The first x% of elements in a linked list, either as an intermediate step or as the final solution.
        - The k-way point/element at a specific position in a linked list, such as the middle element or the element at the start of the second quartile.
        - The kth last element in a linked list.
    2. The problem requires detection of a cycle in a linked list or a sequence of symbols.

However, the two-pointer technique is not suitable when:
    1. The input data cannot be traversed linearly, i.e., it's not in an array, linked list, or a string of characters.
    2. The problem can be solved with two pointers traversing an array or a linked list at the same pace.
"""

from src.linked_list_node import LinkedListNode


def find_square_sum(num):
    _sum = 0
    while num > 0:
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def is_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck on the number '1'


def has_cycle(head: LinkedListNode):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # found the cycle
            return True
    return False


def circular_array_has_loop(nums):
    size = len(nums)
    for i in range(size):
        slow = fast = i
        forward = nums[i] > 0

        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            if slow == fast:
                return True
    return False


# A function to calculate the next step
def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result


# A function to detect a cycle doesn't exist
def is_not_cycle(nums, prev_direction, pointer):
    curr_direction = nums[pointer] >= 0
    if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_happy_number(23))
