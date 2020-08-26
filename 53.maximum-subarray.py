#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
#Top-down Approach:
    # def OPT(self, nums, index):
    #     if index >= len(nums):
    #         return 0
    #     if self.sum[index][0] != None:
    #         return max(self.sum[index][0], self.sum[index][1])
    #     self.sum[index][0] = nums[index] + self.OPT(nums, index+1)
    #     self.sum[index][1] = nums[index]
    #     return max(self.sum[index][0], self.sum[index][1])


    # def maxSubArray(self, nums: List[int]) -> int:
    #     size = len(nums)
    #     self.sum = []
    #     for _ in range(size):
    #         self.sum.append([None, None])
    #     self.OPT(nums, 0)
    #     max_sum = self.sum[0][0]
    #     for index in range(size):
    #         max_sum = max(max_sum, self.sum[index][0], self.sum[index][1])

    #     for index in range(size):
    #         print(f"{self.sum[index][0]}, {self.sum[index][1]}")

    #     return max_sum

#Bottom-up Approach:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        max_sum = nums[-1]
        last = nums[-1]
        for index in range(size-2, -1, -1):
            last = max(nums[index], nums[index] + last)
            max_sum = max(last, max_sum)
        return max_sum
# @lc code=end

