from typing import List

"""
내 논리: 양 리스트에 포인터 p1, p2를 만든 후, p2를 p1에 넣을 수 있는지를 체크하고 넣을 수 있으면 넣고 넣을 수 없으면 p1++ 하기
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        
        p1 = 0
        p2 = 0
        
        sz = m + n
        while p2 < n:
            # p1에 들어갈 수 있는지 체크
            if p1 >= sz - n and nums1[p1] == 0:
                nums1[p1] = nums2[p2]
                p1 += 1
                p2 += 1
            elif nums1[p1] >= nums2[p2]:
                nums1.insert(p1, nums2[p2])
                p2 += 1
                sz += 1
            else:
                p1 += 1

        cnts = 0
        while nums1[-1] == 0:
            if cnts == m:
                break
            nums1.pop()
            cnts += 1
        
        print(nums1)
sol = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol.merge(nums1, m, nums2, n)