#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # visited = set()
        repetition = -1
        total = sum(nums)
        for n in nums:
            # if n in visited:
            #     repetition = n
            #     break
            # else:
            #     visited.add(n)
            abs_n = abs(n)
            if nums[abs_n-1] < 0:
                repetition = abs_n
                break
            else:
                nums[abs_n-1] = -nums[abs_n-1]
        return [repetition, len(nums)*(len(nums)+1)//2 - total + repetition]
        
# @lc code=end

