#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in dictionary.keys():
                dictionary[nums[i]] = i
            else:
                return [dictionary[difference], i]
                

# @lc code=end

