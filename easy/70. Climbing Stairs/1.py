"""
    dp[i]: i스텝 위치의 계단까지 오를 수 있는 경우의 수
    dp[i] = dp[i - 2] + dp[i - 1]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]


        
        