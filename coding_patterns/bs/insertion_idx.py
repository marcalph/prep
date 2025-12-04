from typing import List


def find_the_insertion_index(nums: List[int], target: int) -> int:
    # Write your code here
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
