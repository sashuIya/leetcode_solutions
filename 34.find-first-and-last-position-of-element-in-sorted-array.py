# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

from bisect import bisect_left
from bisect import bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_right(nums, target)

        if l != len(nums) and nums[l] == target:
            return [l, r - 1]

        return [-1, -1]