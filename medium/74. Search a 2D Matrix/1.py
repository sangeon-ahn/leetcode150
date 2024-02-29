"""
    1. 문제 분석
        크기가 n*m인 2차원 격자가 주어지고, 격자의 각 행은 오름차순으로 숫자가 정렬되어 있다.
        타겟 넘버가 주어질 때, 해당 타겟이 격자에 있는지 없는지 판단하는 문제

        조건
        - 시간복잡도 O(mn)으로 풀어야 한다.
        1 <= n,m <= 100
        -1만 <= 숫자 <= 1만

    2. 풀이 방법
        그냥 격자 숫자들을 하나의 리스트에 넣은 다음 -> 이것부터 O(mn)이라 안됨
        log(mn)은 격자 숫자들을 이분탐색해서 타겟 찾아야 가능
        log(m*n) = logm + logn -> 행에 대해 이분탐색 + 열에 대해 이분탐색
        행 이분탐색 하려면 각 행의 첫값을 알아야 함(x)
        
        더작고 더큰것 사이에 오면 됨.
        계산은 solve 함수가 하고,
        행 찾았으면 이제 열에 대해 이분탐색 해서 구하기

        

"""
from typing import List
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        st = 0
        en = n - 1
        
        row = 0

        while st <= en:
            mid = (st + en) // 2

            if matrix[mid][0] > target:
                en = mid - 1
            elif matrix[mid][0] < target:
                row = mid
                st = mid + 1
            else:
                return True
        
        idx = bisect.bisect_left(matrix[row], target)
        
        if idx < 0 or idx >= m:
            return False

        return matrix[row][idx] == target


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
sol = Solution()
ans = sol.searchMatrix(matrix, target)

print(ans)
        
        
                

        