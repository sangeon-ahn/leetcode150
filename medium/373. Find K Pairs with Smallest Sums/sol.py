"""

"""
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hq = []

        for i in range(len(nums1)):
            heapq.heappush(hq, [nums1[i] + nums2[0], i, 0])
        
        ans = []

        while k and hq:
            curSum, idx1, idx2 = heapq.heappop(hq)
            
            ans.append([nums1[idx1], nums2[idx2]])
            k -= 1

            if idx2 + 1 < len(nums2):
                heapq.heappush(hq, [nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1])
        
        print(ans)
        return ans

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

sol = Solution()
ans = sol.kSmallestPairs(nums1, nums2, k)



        