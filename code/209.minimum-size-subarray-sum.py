#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if nums[0] >= s:
            return 1
        if size == 1:
            return 0

        min_length = None
        left, right = 0, 1
        the_sum = nums[0]
        while right < size:
            the_sum += nums[right]
            if the_sum >= s:
                min_length = right - left + 1
                break
            else:
                right += 1
        if min_length == None:
            return 0
        
        while right < size:
            while left <= right and the_sum >= s:
                min_length = min(min_length, right-left+1)
                the_sum -= nums[left]
                left += 1
            right += 1
            if right < size:
                the_sum += nums[right]
                if the_sum >= s:
                    min_length = min(min_length, right-left+1)
        return min_length
        
            

            

# @lc code=end

