#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from itertools import permutations
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_size = len(s)
        p_size = len(p)
        if p_size > s_size:
            return []

        ret = []
        compare = {}
        hash_table = {}
        total = 0
        for i in range(p_size):
            compare[p[i]] = compare.get(p[i], 0) + 1
            hash_table[p[i]] = 0
        for i in range(p_size):
            if s[i] in hash_table.keys():
                hash_table[s[i]] = hash_table[s[i]] + 1
                if hash_table[s[i]] == compare[s[i]]:
                    total = total + compare[s[i]]

        for i in range(s_size-p_size+1):
            if total == p_size:
                ret.append(i)
            if s[i] in hash_table.keys():
                if hash_table[s[i]] == compare[s[i]]:
                    total = total - compare[s[i]]
                hash_table[s[i]] = hash_table[s[i]] - 1
            if i + p_size < s_size:
                j = i + p_size
                if s[j] in hash_table.keys():
                    hash_table[s[j]] = hash_table[s[j]] + 1
                    if hash_table[s[j]] == compare[s[j]]:
                        total = total + compare[s[j]]
        return ret


# @lc code=end

