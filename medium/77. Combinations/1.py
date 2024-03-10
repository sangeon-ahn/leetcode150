"""
    n, k가 주어질 때, 1~n의 숫자들 중 k개를 고르는 조합 다 구하는 문제
    
    내부 함수 만들고 인자로 현재 위치랑 개수 받아서 개수 k개 되면 정답배열에 넣기
    재귀 시작시 append, 끝나면 pop 
"""
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def recur(cur, sz, temp):
            if sz == k:
                ans.append(temp[:])
                return
            
            for num in range(cur, n + 1):
                temp.append(num)
                recur(num + 1, sz + 1, temp)
                temp.pop()
        
        recur(1, 0, [])
        return ans

sol = Solution()
ans = sol.combine(4, 2)

print(ans)
                

        
        