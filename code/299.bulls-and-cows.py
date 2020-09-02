#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            if secret[i] not in cows:
                cows[secret[i]] = 1
            else:
                cows[secret[i]] += 1

        count_cows = 0
        for i in range(len(guess)):
            if guess[i] in cows and cows[guess[i]] > 0:
                cows[guess[i]] -= 1
                count_cows += 1
                
        return f"{bulls}A{count_cows-bulls}B"
        
        
# @lc code=end

