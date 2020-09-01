#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = a & b
            a = (a ^ b) & 0xffffffff
            b = (carry << 1) & 0xffffffff
        if a > 0x7fffffff:
            a = ~(a ^ 0xffffffff)
        return a
# @lc code=end

