from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def trade(day):
            if day == 0:
                return -prices[day], 0 # (-price[0], 0)

            prevHold, prevNotHold = trade(day - 1)

            hold = max(prevHold, prevNotHold - prices[day])
            notHold = max(prevNotHold, prevHold + prices[day])

            return hold, notHold # (-prices[0], 0)
        
        lastDay = len(prices) - 1

        return trade(lastDay)[1]

