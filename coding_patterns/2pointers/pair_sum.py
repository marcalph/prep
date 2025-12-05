from typing import List


def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    if not nums:
        return []
    left, right = 0, len(nums) - 1
    while left < right:
        if (current := nums[left] + nums[right]) == target:
            return [left, right]
        elif current > target:
            right -= 1
        else:
            left += 1
    return []
