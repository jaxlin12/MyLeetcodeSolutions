#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        if root != None:
            self.stack.append(root)


    def next(self) -> int:
        """
        @return the next smallest number
        """
        ptr = self.stack[-1]
        if ptr.left != None:
            while ptr.left != None:
                self.stack.append(ptr.left)
                ptr.left = None
                ptr = self.stack[-1]
        ptr = self.stack.pop()
        if ptr.right != None:
            self.stack.append(ptr.right)
            ptr.right = None
        return ptr.val        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.stack) != 0:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

