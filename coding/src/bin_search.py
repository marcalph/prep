""""
Use this if:
    - the array might be sorted and then rotated around some unknown pivotor some elements might be modified based on a specific condition. 
    - searching for a target satisfying multiple requirements, a modified binary search can be used.
        e. g. finding a range rather than a single target or finding the leftmost or the rightmost occurrence of a target value.
don't use this if:
    - there is no direct addressing
    - non value based solution
"""


def binary_search(nums, target):
    l,r = 0, len(nums)-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            r = mid-1
        else:
            l = mid+1
    # Replace this placeholder return statement with your code
    return mid
