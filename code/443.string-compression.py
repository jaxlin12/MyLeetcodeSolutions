#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        size = len(chars)
        if size == 0:
            return 0
        last_char = chars[0]
        count = 0
        index = 0
        i = 0
        while i < size:
            if chars[i] == last_char:
                count += 1
            else:
                chars[index] = last_char
                if count != 1:
                    num = str(count)
                    for n in num:
                        index += 1
                        chars[index] = str(n)
                index += 1
                last_char = chars[i]
                count = 1
            i += 1
        chars[index] = last_char
        if count != 1:
            num = str(count)
            for n in num:
                index += 1
                chars[index] = str(n)
        index += 1
        return index
            

            
# @lc code=end

