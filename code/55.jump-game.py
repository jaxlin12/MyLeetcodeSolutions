#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        if len(nums) <= 1:
            return True
        if nums[0] == 0:
            return False
        index = 0
        step = nums[index]
        while True:
            index = index + 1
            max_step = nums[index]
            i = 0
            for i in range(index, min(index+step, last_index+1)):
                if nums[i] >= max_step or (i + nums[i]) > (index + max_step):
                    max_step = nums[i]
                    index = i
            if i == last_index:
                return True
            elif max_step == 0:
                return False
            else:
                step = max_step

        
# @lc code=end

