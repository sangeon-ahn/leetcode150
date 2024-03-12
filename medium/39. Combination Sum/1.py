from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        candies = []
        ans = []
        def recur(idx, val):
            if val == target:
                ans.append(candies[:])
                return
            
            if idx >= len(candidates):
                return
            
            for i in range(idx, len(candidates)):
                if val + candidates[i] > target:
                    break

                candies.append(candidates[i])
                recur(i, val + candidates[i])
                candies.pop()
        
        recur(0, 0)
        print(ans)
        return ans

candidates = [2]
target = 1

sol = Solution()
ans = sol.combinationSum(candidates, target)



        