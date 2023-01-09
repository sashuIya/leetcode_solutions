# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def check(v1, v2):
    if not v1 or not v2: 
        # return v1 == v2
        return (not v1 and not v2)
    
    if v1.val != v2.val: return False

    return check(v1.left, v2.right) and check(v1.right, v2.left)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
       return check(root, root) 