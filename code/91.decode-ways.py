#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    # def decode(self, s: str, index) -> int:
    #     size = len(s)
    #     if size == 0:
    #         return 0
    #     elif size == 1:
    #         if s != "0":
    #             return 1
    #         else:
    #             return 0
    #     elif size == 2:
    #         if int(s) in range(1, 27) and "0" not in s:
    #             return 2
    #         elif s[0] == '0':
    #             return 0
    #         elif s == "10" or s == "20":
    #             return 1
    #         elif '0' in s:
    #             return 0
    #         else:
    #             return 1
            
    #     if self.ways[index] != None:
    #         return self.ways[index]

    #     one_char = self.decode(s[0], index) * self.decode(s[1:], index+1)
    #     new_s = s[0:2]
    #     if int(new_s) in range(1, 27) and new_s[0] != "0":
    #         two_char = self.decode(s[2:], index+2)
    #     else:
    #         two_char = 0
    #     self.ways[index] = one_char + two_char
    #     return self.ways[index]

    # def numDecodings(self, s: str) -> int:
    #     self.ways = [None] * len(s)
    #     return self.decode(s, 0)

    # def numDecodings(self, s):
    #         #dp[i] = dp[i-1] if s[i] != "0"
    #         #       +dp[i-2] if "09" < s[i-1:i+1] < "27"
    #         if s == "": return 0
    #         dp = [0 for x in range(len(s)+1)]
    #         dp[0] = 1
    #         for i in range(1, len(s)+1):
    #             if s[i-1] != "0":
    #                 dp[i] += dp[i-1]
    #             if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #"01"ways = 0
    #                 dp[i] += dp[i-2]
    #         return dp[len(s)]

    def numDecodings(self, s):
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w

# @lc code=end

