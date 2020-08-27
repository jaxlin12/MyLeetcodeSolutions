#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth == 0 and right_depth == 0:
            return 1
        elif left_depth == 0:
            return 1 + right_depth
        elif right_depth == 0:
            return 1 + left_depth
        return 1 + min(left_depth, right_depth)


        
# @lc code=end

