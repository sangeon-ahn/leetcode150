"""
    정수 배열이 주어질 때, 합이 가장 큰 subarray를 구해서 합을 반환하라.
    N<=10만
    
    1차원 dp로 풀면 된다.
    dp[i]: 0~i 숫자를 이용해서 만들 수 있는 부분배열의 최대합
    dp[i]: 만약 dp[i-1] > 0이라면 dp[i] = dp[i-1] + nums[i]
    그 외엔 dp[i] = nums[i]
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp배열 생성
        n = len(nums)
        dp = [-float('inf') for _ in range(n)]
        dp[0] = nums[0]

        for i in range(1, n):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        
        return max(dp)
nums = [5,4,-1,7,8]
sol = Solution()
ans = sol.maxSubArray(nums)
print(ans)

        