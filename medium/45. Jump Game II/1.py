from typing import List
"""
    dp[i]
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        if n == 2:
            if nums[0] >= 1:
                return 1
            else:
                return 0
        
        dp = [(0, 0) for _ in range(n)]
        dp[0] = (nums[0], 0)

        for i in range(1, len(nums) - 1):
            if dp[i-1][0] >= n - 1: # n = 5
                return dp[i-1][1] + 1

            if dp[i - 1][0] >= i + nums[i]:
                dp[i] = dp[i-1]
            else:
                dp[i] = (i + nums[i], dp[i][1] + 1)
        return dp[n-2][1]
            
# nums = [2,3,1,1,4]
# nums = [2,3,0,1,4]
# nums = [2,3,1,1,4]
nums = [1, 2]
sol = Solution()
ans = sol.jump(nums)
print(ans)