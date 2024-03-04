from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)] 

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegrees[pre[0]] += 1
        
        dq = deque()

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                dq.append(i)
        
        ans = []

        while dq:
            cur = dq.popleft()
            ans.append(cur)

            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    dq.append(nxt)
        
        if len(ans) == numCourses:
            return ans
        return []

            


        