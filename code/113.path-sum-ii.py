#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dsf(self, root, sum):
        if sum - root.val == 0 and root.left == None and root.right == None:
            return [[root.val]]

        ret = []
        if root.left != None:
            result = self.dsf(root.left, sum - root.val)
            for solution in result:
                solution.append(root.val)
                ret.append(solution)

        if root.right != None:
            result = self.dsf(root.right, sum - root.val)
            for solution in result:
                solution.append(root.val)
                ret.append(solution)
        return ret


    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        ret = self.dsf(root, sum)
        for sol in ret:
            sol.reverse()
        return ret


# @lc code=end

