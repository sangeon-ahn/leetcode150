from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # capMax = min(capital)
        # if w < capMax:
        #     return w

        hq = []

        projects = sorted(zip(profits, capital), key = lambda p:p[1])

        idx = 0
        while k:
            while idx < len(projects) and projects[idx][1] <= w:
                heapq.heappush(hq, -projects[idx][0])
                idx += 1
            
            if hq:
                w -= heapq.heappop(hq)
                k -= 1
            else:
                return w

        # print(w)
        return w


k = 1
w = 2
profits = [1,2,3]
capital = [1,1,2]
sol = Solution()
ans = sol.findMaximizedCapital(k, w, profits, capital)
                