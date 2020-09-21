#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return None
        if size <= 2:
            return min(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, size-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid - 1] > nums[mid] and (mid + 1 == size or nums[mid] < nums[mid + 1]):
                return nums[mid]
            elif nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return None
        
# @lc code=end

