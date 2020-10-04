#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root):
        if root == None:
            return
        self.inOrderTraversal(root.left)
        self.size += 1
        if self.size == self.k:
            self.ret = root.val
            self.found = True
        if self.found:
            return
        self.inOrderTraversal(root.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.size = 0
        self.k = k
        self.ret = None
        self.found = False
        self.inOrderTraversal(root)
        return self.ret

        
# @lc code=end

