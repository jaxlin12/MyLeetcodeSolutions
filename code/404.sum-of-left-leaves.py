#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, is_left):
        if root == None:
            return
        if root.left == None and root.right == None:
            if is_left:
                self.sum += root.val
                return
            else:
                return
        self.traverse(root.left, True)
        self.traverse(root.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum = 0
        self.traverse(root, False)
        return self.sum

# @lc code=end

