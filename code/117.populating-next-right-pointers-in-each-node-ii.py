#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
    def find_next(self, root):
        next_ptr = root.next
        while next_ptr != None and next_ptr.left == None and next_ptr.right == None:
            next_ptr = next_ptr.next

        if next_ptr != None:
            if next_ptr.left != None:
                return next_ptr.left
            elif next_ptr.right != None:
                return next_ptr.right
        else:
            return None
            


    def dsf(self, root):
        
        if root == None or (root.left == None and root.right == None):
            return
        
        if root.left != None:
            if root.right != None:
                root.left.next = root.right
            else:
                root.left.next = self.find_next(root)

        if root.right != None:
            root.right.next = self.find_next(root)
            

        self.dsf(root.right)
        self.dsf(root.left)
        return

    def connect(self, root: 'Node') -> 'Node':
        self.dsf(root)
        return root


# @lc code=end

