#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    # def backtracking(self, index, target) -> List[List[int]]:
    #     if index >= len(self.candidates):
    #         return []
    #     ret = []
    #     for num in range(1, self.dictionary[self.candidates[index]]+1):
    #         difference = target - num * self.candidates[index]
    #         if difference == 0:
    #             ret.append([self.candidates[index] for i in range(num)])
    #             return ret
    #         elif difference < 0:
    #             return ret

    #         for i in range(index+1, len(self.candidates)):
    #             result = self.backtracking(i, difference)
    #             for solution in result:
    #                 for _ in range(num):
    #                     solution.append(self.candidates[index])
    #                 ret.append(solution)
    #     return ret


    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #     ret = []
    #     candidates.sort()
    #     self.dictionary = {}
    #     for i in range(len(candidates)):
    #         frequence = self.dictionary.get(candidates[i], 0)
    #         self.dictionary[candidates[i]] = frequence + 1
    #     self.candidates = list(set(candidates))
    #     for i in range(len(candidates)):
    #         ret += self.backtracking(i, target)
    #     return ret

    def combinationSum2(self, candidates, target):
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
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                            result, target - nums[i])




# @lc code=end

