# https://leetcode.com/problems/permutations

# time complexity: O(n * n!)

def f(i, nums, used, local_res, global_res):
    if i == len(nums):
        global_res.append(local_res[:])
        return
    
    for j, v in enumerate(nums):
        if not used[j]:
            local_res[i] = v
            used[j] = True
            f(i + 1, nums, used, local_res, global_res)
            used[j] = False


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        n = len(nums)
        used = [False] * n
        local_res = [0] * n
        global_res = []

        f(0, nums, used, local_res, global_res)
        return global_res