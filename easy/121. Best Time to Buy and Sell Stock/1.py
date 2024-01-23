from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            if prices[i] > minPrice:
                ans = max(ans, prices[i] - minPrice)
            elif prices[i] < minPrice:
                minPrice = prices[i]

        return ans
# prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
sol = Solution()
ans = sol.maxProfit(prices)

print(ans)

        