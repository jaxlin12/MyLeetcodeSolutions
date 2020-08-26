#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convert(self, nums: List[int], lo, hi) -> TreeNode:
        size = hi - lo
        if size <= 0:
            return None
        mid = lo + size // 2
        head = TreeNode(nums[mid])
        head.left = self.convert(nums, lo, mid)
        head.right = self.convert(nums, mid+1, hi)
        return head

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.convert(nums, 0, len(nums))



# @lc code=end

