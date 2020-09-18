#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildSubTree(self, pre_index, in_start, in_end, dictionary):
        if in_end - in_start == 1:
            return TreeNode(self.preorder[pre_index])
        
        i = dictionary[self.preorder[pre_index]]
        left_start, left_end = in_start, i
        right_start, right_end = i+1, in_end

        root = TreeNode(self.preorder[pre_index])
        if left_end - left_start != 0:
            root.left = self.buildSubTree(pre_index+1, left_start, left_end, dictionary)
        if right_end - right_start != 0:
            root.right = self.buildSubTree(pre_index+left_end-left_start+1, right_start, right_end, dictionary)
        return root
        

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):
            return None
        dictionary = dict(zip(inorder, range(len(inorder))))
        self.preorder = preorder
        self.inorder = inorder
        return self.buildSubTree(0, 0, len(inorder),dictionary)


# @lc code=end

