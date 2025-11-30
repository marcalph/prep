class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        mem = set()
        for i in range(len(nums)):
            if nums[i] not in mem:
                mem.add(nums[i])
                nums[k] = nums[i]
                k += 1

        return k

    def remove_duplicates(self, nums):
        if not nums:
            return 0

        k = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]

        return k + 1  # Length is index + 1
