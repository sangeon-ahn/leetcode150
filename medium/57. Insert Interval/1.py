"""
    겹치지 않는 intervals. interval은 [start, end] 형태이고, start 기준 오름차순 정렬되어 있음.
    newInterval을 intervals에 오름차순 상태 유지하도록 삽입하는데, 병합해서 겹치지 않는 조건 만족시켜야 함. 
"""
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        # 병합 시작 찾기
        n = len(intervals)
        idx = 0
        while idx < n:
            # 겹치면 인덱스 저장(3가지 경우)
            if intervals[idx][0] <= newInterval[0] <= intervals[idx][1]:
                break

            elif newInterval[0] <= intervals[idx][0] and intervals[idx][1] <= newInterval[1]:
                break

            elif intervals[idx][0] <= newInterval[1] <= intervals[idx][1]:
                break

            ans.append(intervals[idx])
            idx += 1
        
        # 병합 할 핊요 없으면 그냥 리턴
        if idx == n:
            ans.append(newInterval)
            ans.sort(key=lambda inter : inter[0])
            return ans

        # 그 외엔 병합
        st = min(intervals[idx][0], newInterval[0])
        en = max(intervals[idx][1], newInterval[1])
        idx += 1

        while idx < n and intervals[idx][0] <= en:
            en = max(en, intervals[idx][1])
            idx += 1
        
        ans.append([st, en])

        for i in range(idx, n):
            ans.append(intervals[i])
        
        return ans

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

sol = Solution()
ans = sol.insert(intervals, newInterval)
        
            
            
            
            
        
        
        

            
                                                                                                                                                                                                  

        