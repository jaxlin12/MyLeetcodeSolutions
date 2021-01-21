#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def search_subtree(self, subroot, target):
        if subroot.left != None:
            if subroot.left == target or self.search_subtree(subroot.left, target):
                return True
                
        if subroot.right != None:
            if subroot.right == target or self.search_subtree(subroot.right, target):
                return True
                
        return False

    def search_supertree(self, root, p, q):
        if root == p:
            return (True, False)
        elif root == q:
            return (False, True)
        else:
            l1 = r1 = l2 = r2 = False
            if root.left != None:
                l1, r1 = self.search_supertree(root.left, p, q)
            if root.right != None:
                l2, r2 = self.search_supertree(root.right, p, q)
            l = l1 or l2
            r = r1 or r2
            if l and r:
                self.result = root
            else:
                return (l, r)
        return (False, False)
                

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p == q:
            return p
        if self.search_subtree(p, q):
            return p
        if self.search_subtree(q, p):
            return q

        self.result = None
        self.search_supertree(root, p, q)
        return self.result
        
# @lc code=end

