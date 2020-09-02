#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = {}
        for i in range(0, len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = i
            else:
                if i - dictionary[nums[i]] <= k:
                    return True
                else:
                    dictionary[nums[i]] = i
        return False
            
# @lc code=end

