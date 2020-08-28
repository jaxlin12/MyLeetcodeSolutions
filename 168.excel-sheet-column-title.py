#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        if n < 1:
            return ""
        if n == 1:
            return "A"
        new_str = ""
        quotient = n
        while quotient > 0:
            remiander = (quotient - 1) % 26
            quotient = (quotient - 1) // 26
            new_str = chr(ord('A') + remiander) + new_str
        return new_str
# @lc code=end

