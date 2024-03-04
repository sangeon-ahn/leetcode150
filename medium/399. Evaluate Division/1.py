"""
    1. 문제 분석
        equations엔 ['a', 'b']같은게 원소로 들어가 있고 values엔 2.0, 3.0같은게 들어가 있다.
        a/b = 2.0이란 뜻이다.
        
        ['a', 'e']같은 query가 주어지는데, a/e를 구하라는 뜻이다.
        0으로 나누거나 equations에 없는 알파벳이 query에 사용될 경우 -1
        그 외엔 값을 구하면 된다.
    
    2. 풀이 방법
        1. 모든 경우의 수에 대해 미리 구해놓아 딕셔너리에 저장 후, 쿼리 돌면서 딕셔너리에서 꺼내오는 방식
        2. 각 쿼리의 시작알파벳에서부터 계산해나가는 방법
"""
from typing import List
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dic2 = defaultdict(list)

        for idx, eq in enumerate(equations):
            dic2[eq[0]].append((eq[1], values[idx]))
            dic2[eq[1]].append((eq[0], 1/values[idx]))
        
        ans = []

        for q in queries:
            st, en = q

            if st not in dic2 or en not in dic2:
                ans.append(-1)  
                continue
            
            if st == en:
                ans.append(1)
                continue

            dq = deque([(q[0], 1)])
            visited = set()
            visited.add(q[0])
            prevAnsSize = len(ans)

            while dq:
                cur = dq.popleft()

                if cur[0] == en:
                    ans.append(cur[1])
                    break

                for nxt in dic2[cur[0]]:
                    if nxt in visited:
                        continue
                    visited.add(nxt)

                    dq.append((nxt[0], cur[1] * nxt[1]))
            
            if prevAnsSize == len(ans):
                ans.append(-1)

        return ans

equations = [["a","b"],["c","d"]]
values = [1.0,1.0]
queries = [["a","c"],["b","d"],["b","a"],["d","c"]]

sol = Solution()
ans = sol.calcEquation(equations, values, queries)
                
                
        
        
        
        

        