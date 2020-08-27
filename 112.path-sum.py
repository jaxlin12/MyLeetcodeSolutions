#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        difference = sum - root.val
        if root.left == None and root.right == None:
            if difference == 0:
                return True
            else:
                return False
        
        return self.hasPathSum(root.left, difference) or self.hasPathSum(root.right, difference)

# @lc code=end

