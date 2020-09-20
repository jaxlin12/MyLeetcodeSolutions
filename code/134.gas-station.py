#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        sum = 0
        current_sum = 0
        start = None
        for i in range(size):
            if start == None:
                start = i
            cost[i] = cost[i] - gas[i]
            current_sum += cost[i]
            if current_sum > 0:
                start = None
                current_sum = 0
            sum += cost[i]
        if sum > 0:
            return -1

        return start



# @lc code=end

