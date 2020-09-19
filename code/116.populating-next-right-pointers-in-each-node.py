#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def dsf(self, root):
        if root == None or root.left == None or root.right == None:
            return
        
        root.left.next = root.right
        if root.next != None:
            root.right.next = root.next.left
        self.dsf(root.left)
        self.dsf(root.right)
        return

    def connect(self, root: 'Node') -> 'Node':
        self.dsf(root)
        return root
        
# @lc code=end

