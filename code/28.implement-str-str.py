#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_size = len(haystack)
        needle_size = len(needle)
        if haystack_size < needle_size:
            return -1
        if needle == "":
            return 0

        index = -1

        for i in range(haystack_size):
            j = 0
            while j < needle_size:
                if i+needle_size > haystack_size or haystack[i+j] != needle[j]:
                    j = -1
                    break
                j = j + 1
            if j == needle_size:
                index = i
                break
        return index
# @lc code=end

