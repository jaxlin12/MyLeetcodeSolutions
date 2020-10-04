#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        size = len(nums)
        if size == 0:
            return []
        elif size == 1:
            return [f"{nums[0]}"]
        
        start = nums[0]
        index = 1
        ret = []
        nums.append(None)
        while index < size+1:
            if nums[index] != nums[index-1] + 1:
                if start == nums[index-1]:
                    ret.append(f"{start}")
                else:
                    ret.append(f"{start}->{nums[index-1]}")
                start = nums[index]
            index += 1
        return ret
        
# @lc code=end

