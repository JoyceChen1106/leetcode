#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        edges ={i:[] for i in range(numCourses)}
        indegress =[0 for i in range(numCourses)]

        for i,j in prerequisites:
            edges[j].append(i)
            indegress[i] += 1

        queue,count = deque([]),0

        for i in range(numCourses):
            if indegress[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            count +=1

            for x in edges[node]:
                indegress[x] -= 1
                if indegress [x]==0:
                    queue.append(x)
        return count == numCourses
    
# @lc code=end

