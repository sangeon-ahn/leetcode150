"""
    맽 밑 배열 크기로 dp 배열을 만든 후, 각 행의 맨 오른쪽에서부터 dp결과를 구하면 된다.

    dp[i]: i번째 위치로 도달하기까지 경로 중 최소비용
    dp[i] = min(dp[i -1], dp[i]) + nums[order][i]
"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [float('inf') for _ in range(len(triangle[-1]))]
        dp[0] = triangle[0][0]

        order = 1
        n = len(triangle)

        while order < n:
            for i in range(len(triangle[order]) - 1, 0, -1):
                dp[i] = min(dp[i - 1], dp[i]) + triangle[order][i]
            
            dp[0] += triangle[order][0]
            order += 1
        
        # print(dp)
        return min(dp)

triangle = [[-10]]
sol = Solution()
ans = sol.minimumTotal(triangle)



        