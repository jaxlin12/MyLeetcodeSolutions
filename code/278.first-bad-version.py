#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        mid = (hi - lo) // 2
        while hi > lo:
            if isBadVersion(mid):
                hi = mid
                mid = lo + (hi - lo) // 2
            else:
                lo = mid + 1
                mid = lo + (hi - lo) // 2
        return mid

        
# @lc code=end

