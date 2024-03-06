from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]) + 1)]] + [[0] + list(map(int, row)) for row in matrix]
        n = len(dp)
        m = len(dp[0])
        ans = 0

        for i in range(1, n):
            for j in range(1, m):
                # (i, j): 정사각형의 맨 왼쪽 맨 아래 위치.
                
                # 0이편 패스
                if dp[i][j] == 0:
                    continue

                # 1인 경우, 위, 아래, 대각선 중 최솟값 + 1
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j])

        return ans

matrix = [["0"]]
sol = Solution()
ans = sol.maximalSquare(matrix)

                

        