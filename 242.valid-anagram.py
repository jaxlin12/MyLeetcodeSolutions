#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dic1, dic2 = {}, {}
        # for item in s:
        #     dic1[item] = dic1.get(item, 0) + 1
        # for item in t:
        #     dic2[item] = dic2.get(item, 0) + 1
        # return dic1 == dic2
        # return sorted(s) == sorted(t)
        freq, dataset = {}, [(s, 1), (t, -1)]
        
        for data, offset in dataset:
            for ch in data:
                freq[ch] = freq.get(ch, 0) + offset

        return not any(freq.values())
        
# @lc code=end

