#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        the_sum = sum(nums)
        return size *(size + 1) // 2 - the_sum
# @lc code=end

