from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        vis = set()
        candies = []

        ans = []
        def recur(depth):
            if depth == len(nums):
                ans.append(candies[:])
                return
            
            for num in nums:
                if num not in vis:
                    vis.add(num)
                    candies.append(num)
                    recur(depth + 1)
                    vis.remove(num)
                    candies.pop()
        recur(0)
        print(ans)
        return ans

nums = [1]
sol = Solution()
ans = sol.permute(nums)
                
        