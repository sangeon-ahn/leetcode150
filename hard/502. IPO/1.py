"""
    리트코드가 IPO를 한다고 치자.
    더 비싸게 팔기 위해 리트코드는 IPO 전에 프로젝트 진행한다.
    최대 k개의 프로젝트 가능
    가장 비싸게 팔기 위해 k개 프로젝트 최고의 경우 구하라.

    조건
    k  100,000 이하
    w 10억 이하
    n 프로핏, 캐피털 개수
    n 10만 이하
    프로핏 1만 이하
    캐피탈 10억 이하

    2. 풀이
    항상 최선의 수만 선택하면 된다.
    우선순위 큐에 정렬기준으로 (profit, capital) 해서 넣기
    pop 해서 capital 부담 가능하면 쓰고 아니면 보관해뒀다가 가능한거 발견시 다시 넣기

    더 최적화 가능?

    
"""
from typing import List
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hq = []
        n = len(profits)

        for i in range(n):
            heapq.heappush(hq, (-profits[i], capital[i]))
        # print(hq)
        profitSum = 0
        st = []

        while k and hq:
            cur = heapq.heappop(hq)
            # print(cur)
            if w + profitSum >= cur[1]:
                profitSum += -cur[0]
                k -= 1

                while st:
                    heapq.heappush(hq, st.pop())
            else:
                st.append(cur)

        # print(profitSum)
        return profitSum + w

k = 1
w = 2
profits = [1,2,3]
capital = [1,1,2]

sol = Solution()
ans = sol.findMaximizedCapital(k, w, profits, capital)

        