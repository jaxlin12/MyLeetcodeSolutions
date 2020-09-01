#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(list(s))
        index = 0
        for char in s:
            if counter[char] == 1:
                return index
            index += 1
        return -1

        
# @lc code=end

