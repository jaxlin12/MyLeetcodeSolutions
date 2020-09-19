#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildSubtree(self, start, end):
        if end < start:
            return None
        if start == end:
            return TreeNode(self.val[start])
        mid = start + (end - start) // 2
        root = TreeNode(self.val[mid])
        root.left = self.buildSubtree(start, mid-1)
        root.right = self.buildSubtree(mid+1, end)
        return root


    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None

        self.val = []
        ptr = head
        while ptr != None:
            self.val.append(ptr.val)
            ptr = ptr.next

        
        return self.buildSubtree(0, len(self.val)-1)

# @lc code=end

