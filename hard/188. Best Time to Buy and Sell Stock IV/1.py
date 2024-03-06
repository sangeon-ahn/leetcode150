from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        steps = [-float('inf') for _ in range(k*2 + 1)]
        steps[0] = 0
        steps[1] = -prices[0]

        for price in prices:
            for i in range(1, len(steps)):
                # 살 때,
                if i % 2 != 0:
                    steps[i] = max(steps[i], steps[i - 1] - price)
                # 팔 때,
                else:
                    steps[i] = max(steps[i], steps[i - 1] + price)
        
        # print(steps)
        return steps[-1]

k = 2
prices = [3,2,6,5,0,3]

sol = Solution()
ans = sol.maxProfit(k, prices)
print(ans)
        
                
        