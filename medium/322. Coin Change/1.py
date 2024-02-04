"""
    각 동전들의 가치가 담긴 coins 리스트와 만들어야 하는 총 가치합amount가 주어질 때, 최소 동전개수로 amount를 만들 때의 동전개수. 못만들면 -1 리턴.
    배낭문제다.
    동전개수: 1이상12이하
    dp[i]: i원을 만드는데 필요한 동전 개수.
    dp[i] = min(dp[i], dp[i-coin] + 1, dp[i-2coin] + 2, ...)
    간단한 방법밖에 생각이 안난다.
    for money
        for coin
            idx = 1
            while money >= idx*coin
    근데 idx 안써도 풀수있었는데 이 풀이가 기억 안난다.
    그냥 for문 돌아도 다 체크되는 풀이었는데,
    일단 대충 기억나는거 있다.
    dp[10] = min(dp[10], dp[10-5] + 1)
    -> 여기서 dp[5]가 1이었고, 1 + 1 = 2라서, dp[10] = 2가 된다.
    따라서 5원짜리 2개가 고려된 상황이다.
    dp의 시작값은 무한대로 둔다.
    dp[0] = 1로 둬야 한다.
"""
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        coins.sort()
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for m in range(1, amount + 1):
            for coin in coins:
                if m < coin:
                    break
                dp[m] = min(dp[m], dp[m - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

coins = [1, 2, 5]
amount = 11
sol = Solution()
ans = sol.coinChange(coins, amount)


        


        