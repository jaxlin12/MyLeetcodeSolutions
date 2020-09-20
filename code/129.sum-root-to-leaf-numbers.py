#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, currentSum):
        if root == None:
            self.sum += currentSum
            return
        
        currentSum = currentSum * 10 + root.val
        if root.left == None and root.right == None:
            self.sum += currentSum
            return
        if root.left != None:
            self.dfs(root.left, currentSum)
        if root.right != None:
            self.dfs(root.right, currentSum)

    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

# @lc code=end

