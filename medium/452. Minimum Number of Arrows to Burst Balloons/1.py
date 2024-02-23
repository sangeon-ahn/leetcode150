"""
    1. 문제 분석
        격자에 풍선이 있다.
        points의 각 원소는 풍선의 가로 영역을 나타낸다.
        화살은 수직으로 쏠 수 있다.(아래에서 위)
        
        x위치에서 화살 쐈을 때, a <= x <= b 인 풍선은 다 터진다.
        화살 쏘는 횟수 제한 없다.

        문제: 모든 풍선을 터뜨리는 데 드는 최소 화살발사 횟수 구하라. 
    
    2. 풀이 방법
        - 풍선 군집들이 있을 것이다.
        - 군집의 정의: 서로 x범위가 겹치는 풍선
        - 겹치는 곳에 화살을 발사해가며 그리디하게 푼다.
        
        - 1. 정렬: (x1좌표 오름차순, x2좌표 내림차순)
        - 2. 순회하며 군집 모으다가, 다음 군집 풍선 나오면 업데이트
        - 3. for문 빠져나오면 군집 하나 존재 -> +1
"""
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p: (p[0], -p[1]))

        ans = 0
        end = points[0][1]

        for p in points[1:]:
            x1, x2 = p

            # 군집 안에 있나 체크
            if x1 <= end:
                end = min(end, x2)
                continue
            
            # 군집 밖에 있으면 이전꺼 터뜨리고 갱신
            ans += 1
            end = x2

        return ans + 1

points = [[1,2],[2,3],[3,4],[4,5]]
sol = Solution()
ans = sol.findMinArrowShots(points)

        