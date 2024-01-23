from typing import List


"""
뒤에서부터 확인하는 방법
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        last = n-1
        for idx in range(n-1, -1, -1):
            if idx + nums[idx] >= last:
                last = idx
        return last == 0