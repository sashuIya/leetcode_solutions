# https://leetcode.com/problems/combination-sum

def f(i, target, nums, local_res, global_res, can_construct):
    if i == len(nums):
        if target == 0:
            global_res.append(local_res[:])
            return True
        return False

    if (i, target) in can_construct and not can_construct[(i, target)]:
        return False

    can_construct[(i, target)] = False

    if f(i + 1, target, nums, local_res, global_res, can_construct):
        can_construct[(i, target)] = True

    if nums[i] <= target:
        local_res.append(nums[i])
        if f(i, target - nums[i], nums, local_res, global_res, can_construct):
            can_construct[(i, target)] = True
        local_res.pop()
    
    return can_construct[(i, target)]


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        local_res = []
        global_res = []
        can_construct = dict()
        f(0, target, candidates, local_res, global_res, can_construct)

        return global_res