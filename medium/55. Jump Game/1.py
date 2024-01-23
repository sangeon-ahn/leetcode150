from typing import List
"""
    dp[i]: i번째에서 가장 멀리 갈 수 있는인덱스
    dp[2] = 4 -> 2번째 위치에서는 4번째까지 갈 수 있다.

    만약 dp[i-1]이 i+1랑 같거나 크면,
        dp[i] = max(dp[i-1], i + nums[i])
    i+1보다 작으면?
        break

    dp[i] >= len(nums) - 1 되는거 있으면 true, 없으면 false
     
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n - 1):
            if dp[i - 1] >= n - 1:
                return True

            if dp[i - 1] >= i:
                dp[i] = max(dp[i - 1], i + nums[i])
            else:
                break

        if dp[n - 2] >= n - 1:
            return True
        return False

nums = [1, 2, 3]
# nums = [3, 2, 1, 0, 4]
sol = Solution()
ans = sol.canJump(nums)
print(ans)