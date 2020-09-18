#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
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
            while i > 1 and nums[i-1] == nums[i-2]:
                i -= 1
            i -= 1
        return dsf
            
    def combine(self, nums: int, k: int) -> List[List[int]]:
        combinations = []
        i = len(nums)
        while i >= k:
            combinations += self.combineNum(nums[:i], k, 1)
            while i > 1 and nums[i-1] == nums[i-2]:
                i -= 1
            i -= 1
        return combinations

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        subset = []
        for k in range(1, size+1):
            subset += self.combine(nums, k)
        subset.append([])
        return subset

# @lc code=end

