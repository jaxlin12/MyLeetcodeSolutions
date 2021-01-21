#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        my_sum = root.val
        if root.left != None:
            my_sum = my_sum + self.dfs(root.left)
        if root.right != None:
            my_sum = my_sum + self.dfs(root.right)
        self.freq[my_sum] = self.freq.get(my_sum, 0) + 1
        return my_sum

    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        self.freq = {}
        self.dfs(root)

        def sort_func(k):
            return self.freq[k]
        ret = sorted(list(self.freq.keys()), key=sort_func, reverse=True)
        stop_index = -1

        for i in range(len(ret)):
            if self.freq[ret[i]] < self.freq[ret[0]]:
                stop_index = i
                break
        if stop_index != -1:
            return ret[:stop_index]
        return ret
            


        
# @lc code=end

