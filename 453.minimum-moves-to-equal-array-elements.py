#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # size = len(nums)
        # the_sum = sum(nums)
        # the_max = max(nums)
        # max_sum = size * the_max
        # move = 0
        # while max_sum != the_sum:
        #     while max_sum > the_sum:
        #         the_sum += size - 1
        #         move += 1
        #     if max_sum < the_sum:
        #         the_max += 1
        #         max_sum = size * the_max
        # return move
        return sum(nums)-min(nums)*len(nums)
        
# @lc code=end

