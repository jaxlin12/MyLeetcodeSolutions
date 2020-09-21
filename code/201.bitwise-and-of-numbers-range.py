#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while(m<n):
            n = n & (n-1)
        return n;

        



# @lc code=end

