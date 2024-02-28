from typing import List
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        size = len(points)
        if size <= 2:
            return size
        
        ans = 0

        for i in range(size):
            dic = defaultdict(int)

            for j in range(i + 1, size):
                p1, p2 = points[i], points[j]

                slope = float('inf') if p1[0] - p2[0] == 0 else p1[1] - p2[1] / p1[0] - p2[0]

                dic[slope] += 1
            
            ans = max(ans, dic[slope] + 1)
        
        return ans
