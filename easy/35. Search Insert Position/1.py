"""
    bisect.bisect_left 해서 찾으면 된다.
"""
from typing import List
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)

        return idx

        