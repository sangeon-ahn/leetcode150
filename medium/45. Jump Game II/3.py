from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [float('inf') for _ in range(n)]
        steps[0] = 0

        for i in range(n):
            cur = nums[i]
            if cur == 0:
                continue

            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    break

                steps[i + j] = min(steps[i + j], steps[i] + 1)
        
        return steps[n - 1]

# nums = [2, 3, 1, 1, 4]
nums = [2, 3, 0, 1, 4]
sol = Solution()
ans = sol.jump(nums)
print(ans)
