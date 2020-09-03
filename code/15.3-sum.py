#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size < 3:
            return []
        nums.sort()

        res = []
        i = 0
        while i < size:
            j = i + 1
            k = size - 1
            target = -nums[i]
            while j < k:
                sum = nums[j] + nums[k]
                if sum == target:
                    res.append((nums[i],nums[j],nums[k]))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif sum < target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
            while i < size and nums[i] == nums[i-1]:
                i += 1
        return res

# @lc code=end

