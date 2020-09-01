#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_table = [0] * 26
        for char in magazine:
            hash_table[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if hash_table[ord(char) - ord('a')] > 0:
                hash_table[ord(char) - ord('a')] -= 1
            else:
                return False
        return True
# @lc code=end

