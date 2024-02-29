from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        st = 0
        en = n * m - 1

        def solve(idx):
            return matrix[idx//n][idx%m]

        while st <= en:
            mid = (st + en) // 2
            val = solve(mid)

            if val < target:
                st = mid + 1
            elif val > target:
                en = mid - 1
            else:
                return True

        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()
ans = sol.searchMatrix(matrix, target)