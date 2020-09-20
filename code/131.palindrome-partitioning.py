#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def isPalindrome(self, s):
        size = len(s)
        left, right = 0, size - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        size = len(s)
        if size == 0:
            return [[]]
        if size == 1:
            return [[s]]
        

        ret = []
        if self.isPalindrome(s):
            ret.append([s])
        for i in range(1, size):
            left = s[:i]
            if self.isPalindrome(left):
                right = s[i:]
                right_ret = self.partition(right)
                for sol in right_ret:
                    sol.insert(0, left)
                    ret.append(sol)
        return ret

# @lc code=end

