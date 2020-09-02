#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size = len(s)
        if size == 0 or numRows == 0:
            return ""
        if numRows == 1 or size <= numRows:
            return s
        new_s = ""
        group_letters = 2 * numRows - 2
        num_of_group = size // group_letters + 1

        group_num = 0
        for i in range(numRows):
            for j in range(num_of_group):
                start = j*group_letters
                if i+start < size:
                    new_s += s[i+start]
                if i != 0 and i != numRows - 1 and (group_letters-i+start) < size:
                    new_s += s[group_letters-i+start]
        return new_s


# @lc code=end

