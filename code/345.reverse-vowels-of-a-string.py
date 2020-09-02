#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        left, right = 0, len(s)-1
        while left < right:
            left_vowels = s[left] in vowels
            right_vowels = s[right] in vowels
            if left_vowels and right_vowels:
                temp = s[right]
                s[right] = s[left]
                s[left] = temp
                left += 1
                right -= 1
            elif not left_vowels and not right_vowels:
                left += 1
                right -= 1
            elif not left_vowels:
                left += 1
            elif not right_vowels:
                right -= 1
        s = "".join(s)
        return s

# @lc code=end

