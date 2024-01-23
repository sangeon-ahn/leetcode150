from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        n = len(nums)
        modK = k % n
        nums[:modK] = reversed(nums[:modK])
        nums[modK:] = reversed(nums[modK:])