#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if 0 <= numCourses <= 1:
            return [numCourses-1]
            
        course = []
        next_course = []
        for i in range(numCourses):
            course.append(set())
            next_course.append(set())
        for pre in prerequisites:
            course[pre[0]].add(pre[1])
            next_course[pre[1]].add(pre[0])

        reachable = []
        visited = [False] * numCourses
        queue = collections.deque()
        for i in range(numCourses):
            if len(course[i]) == 0:
                queue.append(i)
                reachable.append(i)
                visited[i] = True

        while len(queue) != 0:
            c = queue.pop()
            isReachable = True
            for d in course[c]:
                if not visited[d]:
                    isReachable = False
                    break
            if isReachable:
                if not visited[c]:
                    reachable.append(c)
                    visited[c] = True
                for d in next_course[c]:
                    if not visited[d]:
                        queue.append(d)
        if len(reachable) != numCourses:
            return []

        return reachable

        
        
# @lc code=end

