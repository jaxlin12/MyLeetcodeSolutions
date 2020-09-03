#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size < 3:
            return []
        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]
        i = 0
        while i < size:
            j = i + 1
            k = size - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < abs(closest - target):
                    closest = sum
                if sum == target:
                    return sum
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
        return closest



# @lc code=end

