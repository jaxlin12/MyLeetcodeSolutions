#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        a_size = len(a)
        b_size = len(b)
        carry_out = 0
        i = a_size - 1
        j = b_size - 1

        if a_size >= b_size:
            temp_a = a
            temp_b = b
        else:
            temp_a = b
            temp_b = a
            i = b_size - 1
            j = a_size - 1
        new_str = ""
    
        while i >= 0:
            if j >= 0:
                addition = int(temp_a[i]) + int(temp_b[j]) + carry_out
            else:
                addition = int(temp_a[i]) + carry_out
            carry_out = int(addition / 2)
            addition = addition % 2
            new_str = str(addition) + new_str
            i = i - 1
            j = j - 1

        if carry_out > 0:
            new_str = str(carry_out) + new_str
        return new_str
            
# @lc code=end

