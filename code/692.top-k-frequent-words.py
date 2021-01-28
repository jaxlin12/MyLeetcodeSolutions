#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = {}
        for w in words:
            frequency[w] = frequency.get(w, 0) + 1
        def sort_func(a):
            return frequency[a]
        sorted_words = sorted(sorted(set(words)), key=sort_func, reverse=True)
        return sorted_words[:k]
        
# @lc code=end

