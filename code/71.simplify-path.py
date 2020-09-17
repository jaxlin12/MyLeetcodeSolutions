#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        new_path = path.split('/')
        i = 0
        size = len(new_path)
        while i < size:
            if new_path[i] == '':
                new_path.pop(i)
                size -= 1
            elif new_path[i] == '.':
                new_path.pop(i)
                size -= 1
            elif new_path[i] == '..':
                if i == 0:
                    new_path.pop(i)
                    size -= 1
                else:
                    new_path.pop(i-1)
                    new_path.pop(i-1)
                    i -= 1
                    size -= 2
            else:
                i += 1
        new_path.insert(0, '')
        new_str = "/"
        if len(new_path) == 1:
            new_path.insert(0, '')
        return new_str.join(new_path)

# @lc code=end

