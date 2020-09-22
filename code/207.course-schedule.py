#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if 0 <= numCourses <= 1:
            return True
        elif numCourses < 0:
            return False
        course = []
        next_course = []
        for i in range(numCourses):
            course.append(set())
            next_course.append(set())
        for pre in prerequisites:
            course[pre[1]].add(pre[0])
            next_course[pre[0]].add(pre[1])

        reachable = set()
        queue = collections.deque()
        for i in range(numCourses):
            if len(course[i]) == 0:
                queue.append(i)
                reachable.add(i)

        while len(queue) != 0:
            c = queue.pop()
            isReachable = True
            for d in course[c]:
                if d not in reachable:
                    isReachable = False
                    break
            if isReachable:
                reachable.add(c)
                for d in next_course[c]:
                    if d not in reachable:
                        queue.append(d)

        return len(reachable) == numCourses

        
            



# @lc code=end

