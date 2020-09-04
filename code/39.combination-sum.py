#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def backtracking(self, index, target) -> List[List[int]]:
        difference = target - self.candidates[index]
        if difference == 0:
            return [[self.candidates[index]]]
        elif difference < 0:
            return []

        ret = []
        for i in range(index, len(self.candidates)):
            result = self.backtracking(i, difference)
            for solution in result:
                solution.append(self.candidates[index])
                ret.append(solution)
        return ret


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.candidates = candidates
        for i in range(len(candidates)):
            ret += self.backtracking(i, target)
        return ret
        
            



# @lc code=end

