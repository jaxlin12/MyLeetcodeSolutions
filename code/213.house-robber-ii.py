#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def dp(self, index):
        if index >= self.size:
            return 0

        if self.memory[index] != None:
            return self.memory[index]

        self.memory[index] = max(self.nums[index]+self.dp(index+2), self.dp(index+1))
        return self.memory[index]

    def rob(self, nums: List[int]) -> int:
        self.size = len(nums)
        if self.size == 0:
            return 0
        elif self.size == 1:
            return nums[0]
        self.nums = nums
        self.memory = [None] * self.size
        rob1 = self.dp(1)
        self.size -= 1
        self.memory = [None] * self.size
        rob2 = self.dp(0)
        return max(rob1, rob2)

        
# @lc code=end

