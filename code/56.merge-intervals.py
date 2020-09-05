#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        size = len(intervals)
        if size == 0:
            return []
        intervals.sort()
        left, right = intervals[0]
        res = []
        for l, r in intervals:
            if l > right:
                res.append([left, right])
                left = l
                right = r
            elif r > right:
                right = r
        res.append([left, right])
            


        return res


# @lc code=end

