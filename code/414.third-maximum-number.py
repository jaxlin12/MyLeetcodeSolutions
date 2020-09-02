#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    from random import randint
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        
        def get_kth_rank(nums, k):
            """0-indexed (ranks are from 0 (min) to len(nums) - 1 (max).)"""
            pivot = nums[randint(0, len(nums) - 1)]
            left, right = [], []
            
            for x in nums:
                if x < pivot:
                    left.append(x)
                if x > pivot:
                    right.append(x)
            
            if len(left) == k:
                return pivot
            elif len(left) < k:
                return get_kth_rank(right, k - (len(left) + 1))
            else:
                return get_kth_rank(left, k)
            
        return get_kth_rank(nums, len(nums) - 3)

        
# @lc code=end

