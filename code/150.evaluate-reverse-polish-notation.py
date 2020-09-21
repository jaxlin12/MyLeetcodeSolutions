#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == '+':
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                stack.append(lhs + rhs)
            elif s == '-':
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                stack.append(lhs - rhs)
            elif s == '*':
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                stack.append(lhs * rhs)
            elif s == '/':
                rhs = int(stack.pop())
                lhs = int(stack.pop())
                sign = 1
                if lhs < 0 and rhs < 0:
                    sign = 1
                elif lhs < 0 or rhs < 0:
                    sign = -1
                stack.append(abs(lhs) // abs(rhs) * sign)
            else:
                stack.append(s)
        return stack[-1]

# @lc code=end

