# binary search 이용
from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        
        for n in nums[1:]:
            if sub[-1] < n:
                sub.append(n)
            else:
                pos = bisect.bisect_left(sub, n) # n은 없고, n보다 큰 것들 중 가장 작은 숫자의 인덱스를 반환한다.

                sub[pos] = n

        return len(sub)


                
            