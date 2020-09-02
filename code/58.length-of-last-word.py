#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s)-1
        while index >= 0 and s[index] == ' ':
            index = index - 1
        s = s[:index+1]
        if len(s) == 0:
            return 0
        str_arr = s.split(' ')
        return len(str_arr[-1])

# @lc code=end

