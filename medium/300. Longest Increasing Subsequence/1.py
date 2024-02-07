"""
    가장 긴 증가하는 부분수열 구하는 문제
    dp문제다. 일단 각 숫자의 LIS는 기본값이 1으로 둔다. 이후,
    nums 인덱스1부터 for문 돌면서 이전값이 나보다 작으면 dp[이전값] + 1을 자기 값으로 한다. 이렇게 계속한다. 
"""
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        
        ans = 1
        for i in range(1, n):
            idx = i - 1
            while idx >= 0:
                if nums[idx] < nums[i]:
                    if dp[i] < dp[idx] + 1:
                        dp[i] = dp[idx] + 1
                        if ans < dp[i]:
                            ans = dp[i]
                idx -= 1
        
        return ans

nums = [0,1,0,3,2,3]
sol = Solution()
ans = sol.lengthOfLIS(nums)
                
            

        