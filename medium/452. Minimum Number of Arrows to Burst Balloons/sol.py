class Solution:
    def findMinArrowShots(self, points):
        points.sort(key = lambda p : p[1])
        ans = 0
        end = points[0][1]

        for i in range(1, len(points)):
            if end < points[i][0]:
                ans += 1
                end = points[i][1]

        return ans + 1
        