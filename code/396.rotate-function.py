#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        size = len(A)
        if size == 0:
            return 0
        total = sum(A)
        maximum = 0
        for i in range(size):
            maximum = maximum + i * A[i]
        temp = maximum
        for i in range(size):
            temp = temp - size * A[size-i-1] + total 
            if temp > maximum:
                maximum = temp

        return maximum
                


# @lc code=end

