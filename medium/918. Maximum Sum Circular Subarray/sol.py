from typing import List
"""
    답은 두가지 경우가 있다.
    1. 인덱스가 nums를 넘어가지 않는 subarray가 답일 때,
    2. nums를 넘어가는 경우일 때,

    첫번째 경우는 dp를 통해 최대subarray을 구하면 되고,
    두번째 경우는 dp를 통해 최소subarray를 구한 후, 전체 합에서 해당 최솟값을 빼주면 된다.
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxDp = [x for x in nums]
        minDp = [x for x in nums]

        for i in range(1, n):
            if maxDp[i - 1] < 0:
                maxDp[i] = nums[i]
            else:
                maxDp[i] = maxDp[i - 1] + nums[i]
            
            if minDp[i - 1] < 0:
                minDp[i] = minDp[i - 1] + nums[i]
            else:
                minDp[i] = nums[i]
        
        return max(max(maxDp), sum(nums) - min(minDp))
            
            


nums = [5, -3, 5]
sol = Solution()
ans = sol.maxSubarraySumCircular(nums)
print(ans)
                
        