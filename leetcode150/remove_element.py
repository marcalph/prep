class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Pointer for the next position of non-val elements

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Overwrite element at index k
                k += 1

        return k