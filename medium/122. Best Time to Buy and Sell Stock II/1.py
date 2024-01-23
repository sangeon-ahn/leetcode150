from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = prices[-1]
        n = len(prices)

        if n <= 1:
            return 0

        ans = 0
        idx = n - 2

        while idx >= 0:
            if maxPrice > prices[idx]:
                ans += maxPrice - prices[idx]
                maxPrice =  prices[idx]
                idx -= 1
            
            elif maxPrice == prices[idx]:
                idx -= 1
            
            else: # maxPrice < prices[idx]
                maxPrice = prices[idx]
                idx -= 1
        
        return ans
                
# prices = [7, 1, 5, 3, 6, 4]
# prices = [1, 2, 3, 4, 5]
prices = [7, 6, 4, 3, 1]
sol = Solution()
ans = sol.maxProfit(prices)
print(ans)