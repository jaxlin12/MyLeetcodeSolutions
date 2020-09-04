#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        len_hash = {}
        for s in strs:
            size = len(s)
            word_dict = tuple(sorted(s))
            if size not in len_hash:
                len_hash[size] = {word_dict: [s]}
            else:
                if word_dict in len_hash[size]:
                    len_hash[size][word_dict].append(s)
                else:
                    len_hash[size][word_dict] = [s]
        res = []
        for entry in len_hash:
            for words in len_hash[entry]:
               res.append(len_hash[entry][words]) 

        return res

# class Solution:
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()


# @lc code=end

