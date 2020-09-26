#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        i = 0
        j = 0
        new_list = []
        while i < size:
            if (intervals[i][0] <= newInterval[0] <= newInterval[1] <= intervals[i][1]
                 or newInterval[0] <= intervals[i][0] <= intervals[i][1] <= newInterval[1]
                 or newInterval[0] <= intervals[i][0] <= newInterval[1] <= intervals[i][1]
                 or intervals[i][0] <= newInterval[0] <= intervals[i][1] <= newInterval[1]):
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i += 1
            elif newInterval[0] > intervals[i][1]:
                new_list.append(intervals[i])
                i += 1
            elif newInterval[1] < intervals[i][0]:
                new_list.append(newInterval)
                newInterval = None
                break
        while i < size:
            new_list.append(intervals[i])
            i += 1
        if newInterval != None:
            new_list.append(newInterval)
        return new_list
                


        
# @lc code=end

