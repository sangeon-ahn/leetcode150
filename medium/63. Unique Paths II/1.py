"""
    격자에 로봇과 장애물과 목적지가 주어질 때, 로봇이 목적지까지 장애물을 피해 도달할 수 있는 유니크한 경로의 개수를 구하는 문제
    로봇은 아래, 오른쪽으로만 움직일 수 있다.
    장애물=1, 공간=0
    그냥 아래, 오른쪽 일단 dp 추가한 후에 2중for문 돌면서 확인하면 되는거 아닌가?

"""
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(m):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)

        return dp[n - 1][m - 1]

obstacleGrid = [[0,1],[0,0]]
sol = Solution()
ans = sol.uniquePathsWithObstacles(obstacleGrid)        


        

        