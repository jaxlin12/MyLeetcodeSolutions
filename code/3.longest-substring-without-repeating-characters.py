#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size <= 1:
            return size
        left, right = 0, 1
        dictionary = {s[left]:1}
        max_len = 0
        while left < size and right < size:
            check = dictionary.get(s[right], 0)
            if check == 1:
                max_len = max(right-left, max_len)
                dictionary[s[left]] -= 1
                left += 1
            else:
                dictionary[s[right]] = 1
                right += 1
        return max(max_len, right-left)

# @lc code=end

