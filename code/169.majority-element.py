#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candiate = None
        for num in nums:
            if count == 0:
                candiate = num
            if num == candiate:
                count = count + 1
            else:
                count = count - 1
        return candiate
# @lc code=end

