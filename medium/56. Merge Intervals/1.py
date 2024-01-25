"""
    1. 문제 분석
    겹치는 부분을 하나로 합치기

    2. 풀이 방법
    intervals를 순회하며 겹치는지 확인을 해야하기 때문에, end값을 외부에 가지고 있어야 한다. curStart <= end 인 경우 겹치므로 이때 end를 갱신
    그 외에는 [st, end] 정답리스트에 넣고 st, en 갱신
"""
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        ans = []

        st = intervals[0][0]
        en = intervals[0][1]
        
        for i in range(1, n):
            # 언제만 병합? -> i의 시작부분이 사이에 있고 바깥부분은 밖에 있을 때
            if st <= intervals[i][0] <= en and en < intervals[i][1]:
                en = intervals[i][1]
            elif en < intervals[i][0]:
                ans.append([st, en])
                st = intervals[i][0]
                en = intervals[i][1]

        ans.append([st, en])
        return ans

sol = Solution()
ans = sol.merge()


        