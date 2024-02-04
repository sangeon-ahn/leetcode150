from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        step, seen = 0, 1 << amount # amount가 5라면 b = 100000 b를 5(amount)번 right shift시키면 b = 1이 됨. 

        while (seen & 1) != 1:
            cur = seen # 일단 cur 변수 생성해주고,    
            
            for coin in coins:
                # 해당 코인을 사용하는걸 반영해줌.
                cur |= (seen >> coin)
            
            # 다 반영했는데 똑같으면 -1
            if cur == seen:
                return -1
            
            # 다르면 다시 while 수행
            step, seen = step + 1, cur

        # while 나오면 답 구한 것.
        return step

coins = [1, 2, 5]
amount = 11
sol = Solution()
ans = sol.coinChange(coins, amount)

print(ans)