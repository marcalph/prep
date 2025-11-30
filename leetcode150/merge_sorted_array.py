class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, p = m - 1, n - 1, m + n - 1
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[p] = nums1[i1]
                i1 -= 1
            else:
                nums1[p] = nums2[i2]
                i2 -= 1
            p -= 1

        while i2 >= 0:
            nums1[p] = nums2[i2]
            i2 -= 1
            p -= 1
