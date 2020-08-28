#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, str):
        if root == None:
            return
        if root.left == None and root.right == None:
            new_str = str+ f"->{root.val}"
            self.ret.append(new_str[2:])
            return
        new_str = str+ f"->{root.val}"
        self.traverse(root.left, new_str)
        self.traverse(root.right, new_str)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        self.ret = []
        self.traverse(root, "")
        return self.ret


# @lc code=end

