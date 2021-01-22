#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, root):
        if root.right != None:
            self.DFS(root.right)
        root.val = root.val + self.current_sum
        self.current_sum = root.val
        if root.left != None:
            self.DFS(root.left)
        

    def convertBST(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        self.current_sum = 0
        self.DFS(root)
        return root
        
# @lc code=end

