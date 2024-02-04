from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        step, seen = 0, 1<< amount
        while (seen & 1) != 1: # 1011 & 1 == 1
            cur = seen

            # 각 코인에 대해 coin가치만큼 right shift한 값을 cur과 or연산해서 할당함. 
            for coin in coins:
                cur |= seen >> coin # seen을 계속 오른쪽으로 이동시켜가면서 1이 되었을 때 이제 amount를 만들었다는 거니까 while 빠져나가면서 step 리턴

            # cur과 seen이 같다는 것 -> 위 for문에서 cur을 or 연산해서 변경시켰는데 결과를 보니 달라진게 없다는 것: 애초에 seen & 1이 1이 아니므로 amoount를 만들지도 못하는데 더이상 바뀌는게 없다 -> amount 못만듬 -> -1 리턴
            if cur == seen:
                return -1
                
            step, seen = step + 1, cur

        return step