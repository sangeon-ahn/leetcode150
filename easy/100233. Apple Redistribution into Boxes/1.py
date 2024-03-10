"""
    1. 문제 분석
        apple: 크기 n, capacity: 크기 m
        n개의 packs가 있다. i번째 팩은 apple[i]를 포함한다.
        m개의 boxes도 있다. i번째 박스는 capacity[i] 크기다.

        최소 박스 개수 리턴. 재분배 이 n개의 팩을 박스로 

        그냥 apple에 있는거 capacity에 다 채울려면 몇개 최소로 필요한지 구하는 문제
"""
from typing import List
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort()
        ans = 0

        appleSum = sum(apple)

        for i in range(len(capacity) - 1, -1, -1):
            if appleSum <= capacity[i]:
                return ans + 1
            
            appleSum -= capacity[i]
            ans += 1
        return ans
                
            
            

        