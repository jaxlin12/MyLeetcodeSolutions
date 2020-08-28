#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def DP(self, nums: List[int], index):
        if index >= len(nums):
            return 0
        if self.amount[index] == None:
            self.amount[index] = max(self.DP(nums, index + 1), nums[index] + self.DP(nums, index + 2))
        return self.amount[index]

    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        self.amount = [None] * size
        return self.DP(nums, 0)

# @lc code=end

