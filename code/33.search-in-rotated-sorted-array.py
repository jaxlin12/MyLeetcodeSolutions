#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return -1
        if size == 1:
            return -1 if nums[0] != target else 0

        left, right = 0, len(nums)-1
        pivot = -1
        while left < right:
            pivot = left + (right - left) // 2
            if pivot == 0:
                break
            if nums[pivot-1] <= nums[pivot] and nums[pivot+1] < nums[pivot]:
                break
            elif nums[pivot-1] > nums[pivot] and nums[pivot+1] >= nums[pivot]:
                pivot = pivot - 1
                break
            
            if nums[pivot-1] <= nums[-1]:
                right = pivot - 1
            else:
                left = pivot + 1
        
        if nums[0] <= target <= nums[pivot]:
            left = 0
            right = pivot
        elif nums[pivot+1] <= target <= nums[-1]:
            left = pivot+1
            right = size-1
        else:
            return -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
# @lc code=end

