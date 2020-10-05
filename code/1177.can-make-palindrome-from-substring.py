#
# @lc app=leetcode id=1177 lang=python3
#
# [1177] Can Make Palindrome from Substring
#

# @lc code=start
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefixSum = [[0] * 26]
        for i in range(len(s)-1):
            prefixSum[-1][ord(s[i])-ord('a')] += 1 
            prefixSum[-1][ord(s[i])-ord('a')] &= 1
            prefixSum.append(prefixSum[i][:])
        prefixSum[-1][ord(s[-1])-ord('a')] += 1
        prefixSum[-1][ord(s[-1])-ord('a')] &= 1
        
        ret = []
        for l, r, k in queries:
            L = prefixSum[l-1] if l != 0 else [0] * 26
            R = prefixSum[r]
            odd = sum(abs(R[i] - L[i]) for i in range(26))
            ret.append((odd - (r-l+1)%2)//2 <= k)
        return ret

        # N = 26
        # a = ord('a')
        # dp = [[0] * N]
        # for i in range(1, len(s)+1):
        #     new = dp[i-1][:]
        #     j = ord(s[i-1]) - a
        #     new[j] += 1
        #     dp.append(new)
        # ans = []
        # for l, r, k in queries:
        #     L = dp[l]
        #     R = dp[r+1]
        #     ans.append(sum((R[i] - L[i]) & 1 for i in range(N)) // 2 <= k)
        # return ans

# @lc code=end

