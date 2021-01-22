#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, t):
        self.ret = self.ret + str(t.val)            
        if t.left == None and t.right == None:
            return
        self.ret = self.ret + "("
        if t.left != None:
            self.DFS(t.left)
        self.ret = self.ret + ")"
        if t.right != None:
            self.ret = self.ret + "("
            self.DFS(t.right)
            self.ret = self.ret + ")"

    def tree2str(self, t: TreeNode) -> str:
        if t == None:
            return ""
        self.ret = ""
        self.DFS(t)
        return self.ret
        
# @lc code=end

