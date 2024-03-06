
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        A = -prices[0]
        B = float('-inf')
        C = float('-inf')
        D = float('-inf')

        for price in prices:
            A = max(A, -price)
            B = max(B, A + price)
            C = max(C, B - price)
            D = max(D, C + price)

        return D

prices = [3, 1, 6, 1, 2, 3, 4, 5]
sol = Solution()
ans = sol.maxProfit(prices)

"""
A: -3      -3  -3   -3  0   0   0   0   0
B: -inf    0   0    2   2   2   3   3   4   
C: -inf    -3  -3   -3  2   2   2   2   2 
D: -inf    0   0    2   2   2   5   5   6
"""

