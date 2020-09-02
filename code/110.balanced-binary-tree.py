#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if self.result == False:
            return 0
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        if abs(left_depth - right_depth) > 1:
            self.result = False
        return 1 + max(left_depth, right_depth)

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        self.result = True
        self.maxDepth(root)
        return self.result
# @lc code=end