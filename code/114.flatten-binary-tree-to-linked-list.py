#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dsf(self, root):
        if root.left == None and root.right == None:
            self.left_leaf = root
            return

        if root.left != None:
            self.dsf(root.left)
        if root.right != None:
            if self.left_leaf != None:
                self.left_leaf.right = root.right
                self.left_leaf = None
            self.dsf(root.right)
            if root.left != None:
                root.right = root.left
        else:
            root.right = root.left
        root.left = None
        return
        


    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        self.left_leaf = None
        return self.dsf(root)

        
# @lc code=end

