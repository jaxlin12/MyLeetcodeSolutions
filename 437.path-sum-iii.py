#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def findPath(self, root, sum):
    #     if root == None:
    #         return
    #     difference1 = sum - root.val
    #     if difference1 == 0:
    #         self.num += 1

    #     self.findPath(root.left, difference1)
    #     self.findPath(root.right, difference1)

    #     if root not in self.visted:
    #         self.visted[root] = 1
    #     else:
    #         return
    #     difference2 = self.sum - root.val
    #     if difference2 == 0:
    #         self.num += 1
    #     self.findPath(root.left, difference2)
    #     self.findPath(root.right, difference2)

    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     if root == None:
    #         return 0
    #     self.visted = {}
    #     self.visted[root] = 1
    #     self.sum = sum
    #     self.num = 0
    #     self.findPath(root, sum)
    #     return self.num
    
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
# @lc code=end

