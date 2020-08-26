#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        if size == 0:
            return 0

        j = 0
        for i in range(size):
            if nums[i] != val:
                nums[j] = nums[i]
                j = j + 1

        return j



# @lc code=end

