from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    memory = {}
    for i, value in enumerate(nums):
        if (suppl:=target - value) in memory:
            return [memory[suppl], i]
        memory[value]=i
    return []