#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        size = len(s)
        i = size - 1
        while i >= 0:
            if s[i] == "]":
                stack.append("")
            elif s[i] == "[":
                i -= 1
                continue
            elif s[i].isnumeric():
                count = ""
                while i >= 0 and s[i].isnumeric():
                    count = s[i] + count
                    i -= 1
                i += 1
                count = int(count)
                repeat = stack.pop()
                for j in range(count):
                    if len(stack) == 0:
                        stack.append(repeat)
                    else:
                        stack[-1] = repeat + stack[-1]
            else:
                if len(stack) == 0:
                    stack.append(s[i])
                else:
                    stack[-1] = s[i] + stack[-1]
            i -= 1
        ret = ""
        for string in stack:
            ret += string
        return ret
        
# @lc code=end

