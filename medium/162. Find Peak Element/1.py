"""
    1. 분석
    숫자들이 주어질 때, 피크지점의 인덱스를 구하라.
    피크지점: 양 숫자가 자신보다 작다.

    2. 풀이
    st = 0, en = len(nums) - 1으로 하고 이분탐색 진행하는데,
    mid 값 확인해서 st, en보다 작으면 왼쪽으로 좁히기 -> 오른쪽으로 좁히기

    1. st, en보다 크면 양쪽 확인후 떨어지고 있으면 왼쪽으로 좁히고 올라가고 있으면 오른쪽으로 좁히기
    2. st, en보다 작으면 그 사이에 피크 없으면 맨끝 숫자가 피크임 -> 한쪽만 확인해도 됨
    3. st < mid < en : mid 양쪽 확인해서 증가중, 감소중인지 파악 후 증가중이면 오른쪽으로, 감소중이면 왼쪽으로
    4. st 
    
    
    
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        st = 0
        en = len(nums) - 1

        while st <= en:
            mid = (st + en) // 2

            val = nums[mid]
            lVal = nums[mid - 1] if mid - 1 >= 0 else -float('inf')
            rVal = nums[mid + 1] if mid + 1 < len(nums) else -float('inf')

            if lVal < val < rVal:
                st = mid + 1
            elif lVal > val > rVal:
                en = mid - 1
            elif lVal < val and rVal < val:
                return mid
            else:
                en = mid - 1
        
        return -1

nums = [1, 2, 1, 3, 5, 6, 4]
sol = Solution()
ans = sol.findPeakElement(nums)
print(ans)
                
        