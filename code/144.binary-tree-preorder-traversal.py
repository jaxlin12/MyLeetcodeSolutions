#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        queue = collections.deque()
        queue.append(root)
        ret = []
        while len(queue) != 0:
            node = queue.popleft()
            ret.append(node.val)
            if node.right != None:
                queue.insert(0, node.right)
            if node.left != None:
                queue.insert(0, node.left)
            
        return ret
        
# @lc code=end

