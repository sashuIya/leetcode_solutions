# https://leetcode.com/problems/path-sum-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###### O(n^2) solution ######
def dfs_sum(v, s, target_sum):
    if not v:
        return 0

    s += v.val

    result = 0
    if s == target_sum:
        result += 1
    
    result += dfs_sum(v.left, s, target_sum)
    result += dfs_sum(v.right, s, target_sum)

    return result

def dfs(v, target_sum):
    if not v:
        return 0

    result = dfs_sum(v, 0, target_sum)   
    if v.left:
        result += dfs(v.left, target_sum)

    if v.right:
        result += dfs(v.right, target_sum)

    return result

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return dfs(root, targetSum)