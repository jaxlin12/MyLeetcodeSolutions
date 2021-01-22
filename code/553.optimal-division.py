#
# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#

# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return f"{nums[0]}"
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        ret = f"{nums[0]}/({nums[1]}"
        for i in range(2, len(nums)):
            ret = ret + f"/{nums[i]}"
        ret = ret + ")"
        return ret

            
        
# @lc code=end

