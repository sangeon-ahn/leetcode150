"""
    line에 n명의 아이들이 있다.
    각각의 아이들은 ratings라는 배열에서 정수값이 할당되어 있다.
    아이들에게 캔디를 줘야한다.
    
    규칙
    1. 각 아이들은 적어도 하나의 캔디를 가져야 한다.
    2. 더 높은 rating을 가지는 아이들은 이웃보다 캔디를 더 많이 가진다.

    반환
    아이들에게 분배해야 할 최소 캔디 필요량

    1. 풀이 생각
    <첫번째 생각>
    첫번째 숫자에 1 부여하고,
    앞레이팅 > 뒷레이팅: 뒷숫자 -1
    앞레이팅 == 뒷레이팅: 뒷숫자 =앞숫자
    앞레이팅 < 뒷레이팅: 뒷숫자 + 1
"""
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [0 for _ in range(n)]
        ans[0] = 1

        for i in range(1, n):
            # 앞레이팅 > 뒷레이팅
            if ratings[i - 1] > ratings[i]:
                ans[i] = ans[i - 1] - 1
            elif ratings[i - 1] == ratings[i]:
                ans[i] = ans[i - 1]
            else:
                ans[i] = ans[i - 1] + 1
        
        # 최솟값 구함.
        minVal = min(ans)

        # 최솟값이 1이상이면 그냥 합 리턴
        if minVal >= 1:
            return sum(ans)

        # 1 이하면 일단 1과의 차이 구함
        diff = 1 - minVal
        
        # 각 숫자에 해당 차이를 더한 후 반환
        return sum(ans) + n * diff


        

ratings = [1, 2, 2]        
sol = Solution()
ans = sol.candy(ratings)
print(ans)