#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        temp = 1
        for i in range(len(nums)):
            out[i] = temp
            temp = temp * nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * temp
            temp = temp * nums[i]
        return out

# @lc code=end

