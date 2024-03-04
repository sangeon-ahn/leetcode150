"""
    1. 모든 수업을 들을 수 있으면 True, 아니면 False
        선수 과목이 있다.
        prerequisites[i] = [1, 0] 일 때 1을 듣기 위해선 0을 들어야 한다.
        -> indegree = 0인 과목부터 듣는다 -> 위상정렬
    
    2. 풀이 방법
        numCourses만큼 그래프 크기 설정후 prerequisites 돌면서 그래프 생성 및 indegree 갱신
        다 돌았으면 indegree = 0인 과목 deque에 넣고 돌리면서 indegree 1씩 감소. 0이면 deque에 넣기
        
        while 끝났는데 indegree 댜 0 아니면 false, 0이면 true
"""
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        dq = deque()

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])
            indegrees[pre[0]] += 1
        
        for idx, indg in enumerate(indegrees):
            if indg == 0:
                dq.append(idx)
        
        while dq:
            cur = dq.popleft()

            for nxt in graph[cur]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    dq.append(nxt)

        return sum(indegrees) == 0
    
numCourses = 2
prerequisites = [[1,0], [0, 1]]
sol = Solution()
ans = sol.canFinish(numCourses, prerequisites)


                

        