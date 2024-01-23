from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def twoPoint(arr, i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            
            return arr
        

        n = len(nums)
        if k > n:
            k %= n
        
        if k > 0:
            twoPoint(nums, 0, n - 1)
            twoPoint(nums, 0, k - 1)
            twoPoint(nums, k, n - 1)