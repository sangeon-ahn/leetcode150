"""
    1. 문제 분석
    happiness와 k 받음
    큐에 n개의 아이 있고 i번째 아이의 행복은 happiness[i]임
    k개의 아이들 선택원함. k개의 턴이 있음.
    각 턴마다 hapiness 선택하는데 아직 선택되지 않은 행복값이어야 하고 이후 1 줄음. 0까지만 줄 수 있음.

    최대 선택된 행복 합 구해라.

    하나 고르면 나머지 행복값 전부는 -1됨
    
    조건
    n <= 20만
    행복값 <= 100,000,000
    k <= n

    2. 풀이 방법
    일단, 큰수부터 뽑는게 맞고 hapiness 정렬을 시켜준다.
    맨뒤에서부터 뽑으면서 turn을 따로 계산해줌으로써 모두 -1 시키는 시간을 절약한다.
    turn값을 적용한 행복값이 0이 되는 순간 중지하고 값 리턴.

"""
from typing import List
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        turn = 0
        ans = 0

        for i in range(len(happiness) - 1, -1, -1):
            val = happiness[i] - turn

            if val > 0 and k > 0:
                k -= 1
                ans += val
                turn += 1
            else:
                break
            
        return ans
        

sol = Solution()
ans = sol.maximumHappinessSum([7, 50, 3], 3)
print(ans)