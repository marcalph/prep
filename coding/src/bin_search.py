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

def is_bad_version(n, target):
    return n>=target

def first_bad_version(n, target):
    cnt = 0
    l, r = 1, n
    while l<=r:
        mid = l+(r-l)//2
        bad = is_bad_version(mid, target)
        badv = mid
        if bad:
            r = mid-1
        else:
            l=mid+1
        cnt+=1
        print(badv)
    return l


def binary_search_rotated(nums, target):
  # Replace this placeholder return statement with your code
  l, r = 0, len(nums)-1
  while l<=r:
      mid = l+(r-l)//2
      if target==nums[mid]:
        return mid
      if nums[l] <= nums[mid]:
          if nums[l] <= target < nums[mid]:
              r = mid - 1 
          else:
              l = mid + 1 
      else:
          if nums[mid] < target <= nums[r]:
              l = mid + 1
          else:
              r = mid - 1 
  return -1
