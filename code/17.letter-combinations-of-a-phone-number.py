#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                     '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = ['']
        for idx in range(len(digits)):
            result = [prev + l for prev in result for l in digit_map[digits[idx]]]
        return result
        

# @lc code=end

