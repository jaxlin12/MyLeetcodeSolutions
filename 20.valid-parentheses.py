#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left_parentheses = ['(', '{', '[']
        right_parentheses = [')', '}', ']']
        match = {}
        for i in range(len(left_parentheses)):
            match[left_parentheses[i]] = right_parentheses[i]
        stack = []
        for char in s:
            if char in left_parentheses:
                stack.append(char)
            elif char in right_parentheses:
                if len(stack) == 0 or char != match[stack.pop()]:
                    return False
        if len(stack) != 0:
            return False
        return True
        
                    
                
            
# @lc code=end

