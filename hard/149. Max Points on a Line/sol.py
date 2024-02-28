from typing import List
from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort()
        dic = defaultdict(int)
        ans = 0

        def gcd(n1, n2):
            if n1 > n2:
                n1, n2 = n2, n1
            
            if n1 % n2 == 0:
                return n2
            return gcd(n1, n2 % n1)

        for i in range(len(points)):
            dic.clear()

            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]

                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]

                key = (0, 0)
                if dx == 0:
                    key = (1, 0)
                elif dy == 0:
                    key = (0, 1)
                else:
                    minDiv = gcd(dx, dy)
                    key = (dx//minDiv, dy//minDiv)

                dic[key] += 1
                ans = max(ans, dic[key])
                
        return ans + 1

points = [[1,1],[2,2],[3,3]]
sol = Solution()
ans = sol.maxPoints(points)
print(ans)