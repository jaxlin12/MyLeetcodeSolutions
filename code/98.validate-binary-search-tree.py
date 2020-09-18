#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root: TreeNode) -> bool:
        if root == None:
            return
        if root.left != None:
            if root.left.val >= root.val:
                self.isBST = False
                return
        if root.right != None:
            if root.right.val <= root.val:
                self.isBST = False
                return
        self.check(root.left) 
        self.inorder.append(root.val)
        self.check(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.inorder = []
        self.isBST = True
        self.check(root)
        if self.isBST == False:
            return False
        else:
            i = 1
            print(self.inorder)
            while i < len(self.inorder):
                if self.inorder[i] <= self.inorder[i-1]:
                    return False
                i += 1
            return True


# @lc code=end

