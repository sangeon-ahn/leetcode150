"""
    3, 0, 6, 1, 5 입력이 들어온 경우, 답은 3이다.
    3번 이상 인용당한 사람이 3명이므로 조건에 만족한다.
    x번 인용당한 사람의 수를 구하고자 할 때, x가 커질수록 인용당한 사람 수는 적어지고 작아질수록 증가한다 -> 파라메트릭 서치
    x축을 인용횟수로 둔 후 시작점을 0, 끝점을 1000으로 둔다. 이후 mid 이상 인용된 사람의 수를 구해서 조건을 만족하는지 본다.
    조건을 만족한다면, 더 큰 h값을 찾기 위해 시작점을 mid + 1로 바꾼다.
"""
from typing import List
class Solution:
    def solve(self, mid, arr):
        res = 0

        for n in arr:
            if n >= mid:
                res += 1
        return res
    
    def hIndex(self, citations: List[int]) -> int:
        st = 0
        en = 1000
        ans = 0
        while st <= en:
            mid = (st + en) // 2

            val = self.solve(mid, citations)
            if val >= mid:
                st = mid + 1
                ans = max(ans, mid)
            else:
                en = mid - 1
        
        return ans


citations = [3, 0, 6, 1, 5]
sol = Solution()
ans = sol.hIndex(citations)

print(ans)