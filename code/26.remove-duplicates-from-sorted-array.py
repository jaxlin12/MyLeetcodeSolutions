#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        j = 0
        for i in range(1, size):
            if nums[i] != nums[j]:
                j = j + 1
                nums[j] = nums[i]
            
        return j + 1
            
# @lc code=end

