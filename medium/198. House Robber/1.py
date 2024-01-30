"""
    1. 문제 분석
        나는 도둑이고 각 집의 돈을 털어야 한다.
        근처 집에 보안 시스템 있으면 멈춰야 함.
        인접 두 집이 같은 밤에 broken되면 경찰만남.
        정수배열 nums에 각 집의 돈. 하룻밤에 최대 털 수 있는 돈합을 구해라.
        붙어 있는 집을 털면 끝
    
    2. 풀이 접근
        일단, 0번 인덱스에서 오른쪽으로 진행되어야 함.
        dp로 풀 수 있을 듯.
        0~X까지의 집을 턴다고 할 때, X번째 집 털면 X-1번째 집 못털음.
        X번째 집 털면, X-2번째 집 텀)
        -> dp[X] = max(dp[X-1], dp[X-2] + nums[X])
        nums = [2, 7, 9, 3, 1]에 대해 성립.
        
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. dp 배열 생성
        n = len(nums)
        dp = [0 for _ in range(n + 1)]
        dp[1] = nums[0]

        # dp 채우기
        for i in range(2, n + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i - 1])
        
        # 답 리턴
        return dp[n]
    
nums = [2, 7, 9, 3, 1]
sol = Solution()
ans = sol.rob(nums)

print(ans)
        