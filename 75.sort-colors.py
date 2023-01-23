# Problem statement:
# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Solution:
        # Will place 0s in the beginning, 2s in the end. 1s will
        # occupy all the rest.
        
        # `pos` defines where to put next 0 and 2. `pos[1]` is not used.
        pos = [0, 0, len(nums) - 1]
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i >= pos[0]:
                nums[pos[0]], nums[i] = nums[i], nums[pos[0]]
                pos[0] += 1
                i -= 1
            elif nums[i] == 2 and i <= pos[2]:
                nums[pos[2]], nums[i] = nums[i], nums[pos[2]]
                pos[2] -= 1
                i -= 1
            i += 1

        return nums