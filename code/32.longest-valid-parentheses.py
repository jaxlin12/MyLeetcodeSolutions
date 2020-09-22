#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack = [-1]
        # sublength = 0
        # maximum = 0
        # i = 0
        # for c in s:
        #     if c == ')' and len(stack) != 1:
        #         stack.pop()
        #         start = stack[-1]
        #         sublength = i - start
        #         maximum = max(sublength, maximum)
        #     elif c == ')':
        #         stack.pop()
        #         if len(stack) == 0:
        #             stack.append(i)
        #     else:
        #         stack.append(i)
        #     i += 1

        # return maximum
        left = right = 0
        maximum = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if right > left:
                left = right = 0
            elif right == left:
                maximum = max(maximum, right * 2)
        
        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if left > right:
                left = right = 0
            elif left == right:
                maximum = max(maximum, left * 2)
        return maximum
        
# @lc code=end

