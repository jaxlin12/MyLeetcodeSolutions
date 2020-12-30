#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph[-1].isalpha():
            paragraph += " "
        words = {}
        w = ""
        max_word = ""
        max_freq = -1
        for char in paragraph:
            if not char.isalpha():
                words[w] = words.get(w, 0)+1
                if words[w] > max_freq and w not in banned and w != "":
                    max_freq = words[w]
                    max_word = w
                w = ""
            else:
                char = char.lower()
                w += char
        return max_word
        
# @lc code=end

