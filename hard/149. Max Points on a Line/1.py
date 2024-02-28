"""
    1. 문제 분석
        유니크한 점들이 주어질 때, 점을 이어서 선분을 그을 때 해당 선분 내에 가장 많은 점이 있는 경우 점의 개수 구하기
    2. 풀이
        직선: y절편과 dx,dy값으로 특정 가능
        점들 2중 for문 돌면서 dx,dy와 y절편 구해서 이값을 튜플로 만들고 값을 점들을 포함하는 리스트로 만든다.
        for문 다 돈 후, 리스트 크기 가장 큰게 답.
        

"""
from typing import List
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dic = defaultdict(list)

        def gcd(n1, n2):
            if n1 % n2 == 0:
                return n2
            return 
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                
                dx, dy = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
                
                tempDx = min(dx, dy)
                tempDy = max(dx, dy)
                
                minDiv = gcd(min(tempDx, tempDy))
                key = 
                if key not in dic:
                    dic[key].append(p1)

                



        