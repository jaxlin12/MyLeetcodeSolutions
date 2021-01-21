#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        def sort_func(k):
            return freq[k]
        ret = sorted(list(freq.keys()), key=sort_func)
        ret_str = ""
        for i in range(len(ret)-1, -1, -1):
            for j in range(freq[ret[i]]):
                ret_str = ret_str + ret[i]
        return ret_str
        
# @lc code=end

