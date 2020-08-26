#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0 or target <= nums[0]:
            return 0

        index = 0
        for index in range(1, size):
            if target <= nums[index]:
                return index
        return index + 1
# @lc code=end

