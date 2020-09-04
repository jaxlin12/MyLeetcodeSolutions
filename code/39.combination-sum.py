#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    # def backtracking(self, index, target) -> List[List[int]]:
    #     difference = target - self.candidates[index]
    #     if difference == 0:
    #         return [[self.candidates[index]]]
    #     elif difference < 0:
    #         return []

    #     ret = []
    #     for i in range(index, len(self.candidates)):
    #         result = self.backtracking(i, difference)
    #         for solution in result:
    #             solution.append(self.candidates[index])
    #             ret.append(solution)
    #     return ret


    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     ret = []
    #     self.candidates = candidates
    #     for i in range(len(candidates)):
    #         ret += self.backtracking(i, target)
    #     return ret

    def combinationSum(self, candidates, target):
        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result
        
    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider 
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return
        
        for i in range(start, len(nums)):
            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i, path + [nums[i]], 
                            result, target - nums[i])
        
            



# @lc code=end

