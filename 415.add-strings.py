#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        size1 = len(num1)
        size2 = len(num2)
        i = size1 - 1
        j = size2 - 1
        carry = 0
        ret = ""
        while i >= 0 and j >= 0:
            add = ord(num1[i]) + ord(num2[j]) - 2 * ord('0') + carry
            carry = add // 10
            ret += str(add % 10)
            i -= 1
            j -= 1
        while i >= 0:
            add = ord(num1[i]) - ord('0') + carry
            carry = add // 10
            ret += str(add % 10)
            i -= 1
        while j >= 0:
            add = ord(num2[j]) - ord('0') + carry
            carry = add // 10
            ret += str(add % 10)
            j -= 1
        if carry != 0:
            ret += str(carry)
        return ret[::-1]
# @lc code=end

