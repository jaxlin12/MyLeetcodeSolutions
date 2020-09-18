#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go(self, root):
        if root == None:
            return
        self.go(root.left)
        self.ret.append(root.val)
        self.go(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ret = []
        self.go(root)
        return self.ret
        
# @lc code=end

