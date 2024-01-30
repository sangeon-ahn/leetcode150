"""
    1. 문제 분석
        n개의 수직선 길이가 담긴 height 받음.
        height[i]: x=i인 지점에 위치한 수직선의 길이    

        수직선 사이 공간에 가장 많은 물을 담을 수 있는 경우의 물 양을 구하라..
    
    2. 풀이 방법
        투포인터로 st, en 정의 후 조여가면서 넓이 계산
        투포인터 이동 규칙: 양쪽 중 더 긴걸로 갱신 -> 이게 아니고, 최솟값이 더 커지는 방향으로.
"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        st = 0
        en = len(height) - 1
        ans = 0

        while st < en:
            h = min(height[st], height[en])
            ans = max(ans, h * (en - st))

            # 일단, 작, 크 있을 때, 작 기준으로 영역 계산되니까 작을 움직여야 더 큰 값 볼 확률이 생긴다.
            if height[st] >= height[en]:
                en -= 1
            else:
                st += 1

        return ans

height = [1,8,6,2,5,4,8,3,7]
# height = [1, 1]
sol = Solution()
ans = sol.maxArea(height)
print(ans)
            
        