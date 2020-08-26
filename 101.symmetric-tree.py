#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False

        return self.isSameTree(root.left, root.right)
        


# @lc code=end

