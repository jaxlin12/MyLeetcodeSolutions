#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        size = len(s)
        pow_of_26 = 1
        num = 0
        for i in range(size-1, -1, -1):
            num = num + pow_of_26 * (ord(s[i]) - ord("A") + 1)
            pow_of_26 = pow_of_26 * 26
        return num

# @lc code=end

