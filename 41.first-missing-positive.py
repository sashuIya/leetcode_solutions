# Problem statement
# https://leetcode.com/problems/first-missing-positive/

# Solution illustration:
# https://github.com/sashuIya/leetcode_solutions/blob/master/images/41.first-missing-positive.png

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] >= 1 and nums[i] <= len(nums):
                # Want to place nums[i] on its place.

                # Skip if it's already on the right place.
                if i == nums[i] - 1: break

                # Skip if right place is already occupied with the right number.
                if nums[i] == nums[nums[i] - 1]: break

                # Place nums[i] on its place.
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        if nums[0] != 1: return 1

        for i, v in enumerate(nums):
            if i != 0 and nums[i] != i + 1:
                return i + 1

        return len(nums) + 1