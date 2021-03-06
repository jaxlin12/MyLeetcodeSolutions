#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


# @lc code=end

