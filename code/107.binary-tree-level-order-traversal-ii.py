#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root, level):
        if root == None:
            return
        if level == len(self.list):
            self.list.insert(0, [])
        self.list[-(level+1)].append(root.val)
        self.traverse(root.left, level+1)
        self.traverse(root.right, level+1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.list = []
        self.traverse(root, 0)
        return self.list

        

# @lc code=end

