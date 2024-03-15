"""
    1. 분석
    왼쪽으로 당겨지도록 회전된다. -> 0번째 인덱스와 마지막 인덱스 비교했을 때 0번째가 더 작다면 회전 안된 것.
    
    2. 풀이
    - k를 구한다.
        - 기울기가 -인 지점을 이분탐색으로 구한다.
    - nums[0]보다 작으면 k ~ len(nums) - 1 사이에서 이분탐색
    - nums[0] 이상이면 0~len(nums)에서 이분탐색
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
            

        st, en = 0, len(nums) - 1

        # k 구하기
        k = 0
        prev = nums[0]
        if nums[0] > nums[-1]:
            while st <= en:
                mid = (st + en) // 2
                
                # mid, mid+1 비교
                if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                    k = mid
                    break
                elif nums[mid] < prev:
                    prev = nums[mid]
                    en = mid - 1
                else:
                    prev = nums[mid]
                    st = mid + 1
        else:
            k = len(nums) - 1

        # print(k)

        if target < nums[0]:
            st = k + 1
            en = len(nums) - 1
        else:
            st = 0
            en = k
            
        while st <= en:
            mid = (st + en) // 2
            
            if nums[mid] == target:
                return mid                
            elif nums[mid] > target:
                en = mid - 1
            else:
                st = mid + 1

        return -1

nums = [8, 9, 2, 3, 4]
target = 9

sol = Solution()
ans = sol.search(nums, target)
print(ans)
            
        