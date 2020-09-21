#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        
        maximum = max(nums)
        if nums[-1] >= 0:
            positive = nums[-1]
            negative = 0
        else:
            positive = 0
            negative = nums[-1]
        for i in range(size-2, -1, -1):
            if nums[i] >= 0:
                new_positive = nums[i] * max(1, positive)
                new_negative = nums[i] * min(0, negative)
            else:
                new_positive = nums[i] * min(0, negative)
                new_negative = nums[i] * max(1, positive)
            positive = new_positive
            negative = new_negative
            maximum = max(maximum, positive)

        return maximum

# @lc code=end

