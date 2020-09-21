#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def binarySearch(self, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        if ((mid - 1) < 0 or self.nums[mid-1] < self.nums[mid]) and ((mid + 1) >= self.size or self.nums[mid+1] < self.nums[mid]):
            return mid
        if (self.nums[mid] > self.nums[mid + 1]):
            return self.binarySearch(left, mid-1)
        return self.binarySearch(mid+1, right)

    def findPeakElement(self, nums: List[int]) -> int:
        self.size = len(nums)
        self.nums = nums
        return self.binarySearch(0, self.size-1)
# @lc code=end

