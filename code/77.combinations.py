#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combineNum(self, nums, k, l):
        size = len(nums)
        if k == l:
            return [[nums[-1]]]
        i = size - 1
        dsf = []
        while i >= k-l:
            ret = self.combineNum(nums[:i], k, l+1)
            for result in ret:
                result.append(nums[-1])
                dsf.append(result)
            i -= 1
        return dsf
            
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        combinations = []
        i = n
        while i >= k:
            combinations += self.combineNum(nums[:i], k, 1)
            i -= 1
        return combinations



# @lc code=end

