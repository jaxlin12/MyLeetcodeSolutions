#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dictionary = {}
        count = 0
        if k == 0:
            freq = {}
            for i in nums:
                freq[i] = freq.get(i, 0) + 1
                if freq[i] == 2:
                    count = count + 1
            return count
            
        for i in nums:
            if dictionary.get(i, False):
                continue
            if dictionary.get(i+k, False):
                count = count + 1
            if dictionary.get(i-k, False):
                count = count + 1
            dictionary[i] = True
        return count
        
# @lc code=end

