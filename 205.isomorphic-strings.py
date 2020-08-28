#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # char1 = [None] * 256
        # char2 = [None] * 256
        # for i in range(len(s)):
        #     if char1[ord(s[i])] == None:
        #         char1[ord(s[i])] = ord(t[i])
        #     else:
        #         if char1[ord(s[i])] != ord(t[i]):
        #             return False
        #     if char2[ord(t[i])] == None:
        #         char2[ord(t[i])] = ord(s[i])
        #     else:
        #         if char2[ord(t[i])] != ord(s[i]):
        #             return False
        # return True
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

# @lc code=end

