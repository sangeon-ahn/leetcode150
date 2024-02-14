from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals + [newInterval]
        intervals.sort(key = lambda inter:inter[0])
        
        ans = [intervals[0]]

        for st, en in intervals[1:]:
            if st <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], en)
            else:
                ans.append([st, en])

        return ans

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

sol = Solution()
ans = sol.insert(intervals, newInterval)
        