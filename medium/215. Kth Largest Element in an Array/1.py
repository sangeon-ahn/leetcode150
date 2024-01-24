"""
    정수 배열 nums와 정수 k가 주어질 때, k번째로 큰 숫자를 구해라.
    정렬 없이 풀 수 있니?
"""
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 1. 최대힙에 넣고 k번 빼는 방법 O(NlogN)
        hq = []
        for n in nums:
            heapq.heappush(hq, -n)
        
        for _ in range(k-1):
            heapq.heappop(hq)
        
        return -heapq.heappop(hq)
            


        # 2. 정렬없이?

        # [3, 2, 1, 5, 6, 4]
        # [1, 2, 3, 4, 5, 6]

        