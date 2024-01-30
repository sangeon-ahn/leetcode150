"""
    1. 문제 분석
        m*n 격자의 맨왼쪽 맨끝 -> 맨오른쪽 맨아래 경로 중, 경로 비용이 가장 작을 때의 비용을 구해라
        
        이동규칙: 오직 오른쪽 or 아래로만 이동 가능
        셀은 모두 0 이상
        1 <= m, n <= 200
    
    2. 풀이 방법
        격자에 첫행과 첫열을 추가하는데 값을 무한대로 초기화.
        이후, board[1][1]부터 시작해서 2차원 dp를 채움

        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + board[i][j]

        추가 행,열 추가할 필요 없이, 첫행, 첫열만 dp배열 세팅해주고 나머지 영역 시작하면 됨.

        내가 문제를 잘못 이해했다. 내 배경지식이 있었기에 정확히 읽어보지 않은 채, 그저 맨오른쪽, 맨아래 셀에 도달했을

        저것도 잘못생각했다. 내가 생각했던게 맞았고 틀린점은 초기 dp세팅할 때 누적합으로 했어야 한 것이다. 누적합을 위해 초기값을 0으로 초기화하기만 하면 된다.
"""
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 1. n, m 구함
        n = len(grid)
        m = len(grid[0])

        # 2. dp배열 생성
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        dp[1][1] = grid[0][0]

        # 3. 초기 dp 세팅
        for i in range(2, n + 1):
            dp[i][1] = dp[i-1][1] + grid[i-1][0]
        for j in range(2, m + 1):
            dp[1][j] = dp[1][j-1] + grid[0][j-1]

        # 4. dp 채우기
        for i in range(2, n + 1):
            for j in range(2, m + 1):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        return dp[n][m]

grid = [[1,3,1],[1,5,1],[4,2,1]]
sol = Solution()
ans = sol.minPathSum(grid)
print(ans)        

        