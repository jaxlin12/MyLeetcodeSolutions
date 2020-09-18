#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        stack = [root]
        ret = []
        new_level = root

        while len(stack) != 0:
            ptr = stack.pop(0)
            if ptr == new_level:
                new_level = None
                ret.append([])
            ret[-1].append(ptr.val)
            if ptr.left != None:
                stack.append(ptr.left)
                if new_level == None:
                    new_level = ptr.left
            if ptr.right != None:
                stack.append(ptr.right)
                if new_level == None:
                    new_level = ptr.right

        return ret


# @lc code=end

