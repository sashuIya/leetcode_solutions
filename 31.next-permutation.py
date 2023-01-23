# Problem statement:
# https://leetcode.com/problems/next-permutation/

# Solution illustration:
# https://github.com/sashuIya/leetcode_solutions/blob/master/images/31.next-permutation.png

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # now: nums[j] > num[i]

            nums[i], nums[j] = nums[j], nums[i]
        
        p1, p2 = i + 1, len(nums) - 1
        while p1 <= p2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 -= 1

        return nums
