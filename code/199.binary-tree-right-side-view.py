#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        max_depth = 0
        stack = [(root, 1)]
        ret = []
        while len(stack) != 0:
            ptr, depth = stack[-1]
            if depth > max_depth:
                ret.append(ptr.val)
                max_depth += 1
            if ptr.right != None:
                stack.append((ptr.right, depth+1))
                ptr.right = None
            elif ptr.left != None:
                stack.append((ptr.left, depth+1))
                ptr.left = None
            else:
                stack.pop()
        return ret

# @lc code=end

