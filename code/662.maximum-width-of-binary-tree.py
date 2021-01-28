#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root == None:
            return 0
        max_width = 0
        
        BFS_queue = deque()
        node_num = 1
        BFS_queue.append((root, node_num))
        current_level_min = 1
        next_level_min = None
        level_count = 2
        while (len(BFS_queue) != 0):
            subroot, num = BFS_queue.popleft()
            if num >= level_count:
                current_level_min = next_level_min
                next_level_min = None
                level_count = level_count * 2
            if subroot.left != None:
                BFS_queue.append((subroot.left, num*2))
                if next_level_min == None:
                    next_level_min = num * 2
            if subroot.right != None:
                BFS_queue.append((subroot.right, num*2+1))
                if next_level_min == None:
                    next_level_min = num * 2 + 1

            if num - current_level_min + 1 > max_width:
                max_width = num - current_level_min + 1
        return max_width
        

# @lc code=end

