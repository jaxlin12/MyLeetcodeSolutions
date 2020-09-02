#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = num & 0xffffffff
        print(num)
        ret = ""
        while num > 0:
            remainder = num % 16
            if remainder >= 10:
                remainder = chr(ord('a') + (remainder - 10))
            else:
                remainder = str(remainder)
            ret += remainder
            num //= 16
        new_ret = ""
        return ret[::-1]
# @lc code=end

