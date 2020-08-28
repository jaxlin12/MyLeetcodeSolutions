#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = None
        if p.val == root.val:
            return root
        elif q.val == root.val:
            return root
        
        if p.val < root.val and q.val < root.val:
            found = self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            found = self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

        return found
# @lc code=end

