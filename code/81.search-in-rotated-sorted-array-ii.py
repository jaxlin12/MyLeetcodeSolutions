#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        if size == 0:
            return False
        if size == 1:
            return nums[0] == target
        if size == 2:
            return nums[0] == target or nums[1] == target
            
        i = size - 1
        while i > 0 and nums[i] == nums[i-1]:
            i -= 1
        if i == 0:
            return nums[0] == target

        left = 0
        right = i
        mid = None

        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return True
            if mid == 0 or mid == size - 1:
                break
            if nums[mid - 1] > nums[mid] and nums[mid + 1] >= nums[mid]:
                break
            if nums[mid] >= nums[i]:
                left = mid + 1
            else:
                right = mid - 1
                
        if target == nums[mid]:
            return True
        if mid == 0:
            left = 0
            right = size - 1
        elif nums[0] <= target <= nums[mid-1]:
            left = 0
            right = mid - 1
        else:
            left = mid
            right = size - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        
# @lc code=end

