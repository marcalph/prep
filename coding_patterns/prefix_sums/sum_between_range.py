from typing import List


class SumBetweenRange:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sum_range(self, i: int, j: int):
        return self.prefix_sum[j] - self.prefix_sum[i - 1] if i - 1 >= 0 else self.prefix_sum[j]
