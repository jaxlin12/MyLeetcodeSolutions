#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        new_string = ""
        size = len(words)
        for i in range(size-1, -1, -1):
            if words[i] != "":
                new_string = new_string + words[i] + " "
        return new_string[:-1]
        
# @lc code=end

