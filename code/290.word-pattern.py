#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_arr = str.split(' ')
        if len(pattern) != len(str_arr):
            return False
        dictionary = {}
        for i in range(len(pattern)):
            if pattern[i] not in dictionary:
                dictionary[pattern[i]] = str_arr[i]
            else:
                if dictionary[pattern[i]] != str_arr[i]:
                    return False
        return len(set(pattern)) == len(set(str_arr))
# @lc code=end

