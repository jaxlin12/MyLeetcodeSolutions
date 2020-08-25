#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {}
        dictionary['I'] = 1
        dictionary['V'] = 5
        dictionary['X'] = 10
        dictionary['L'] = 50
        dictionary['C'] = 100
        dictionary['D'] = 500
        dictionary['M'] = 1000

        size = len(s)
        num = 0
        for i in range(size):
            if i + 1 < size and dictionary[s[i+1]] > dictionary[s[i]]:
                num = num - dictionary[s[i]]
            else:
                num = num + dictionary[s[i]]
        return num

            
# @lc code=end

