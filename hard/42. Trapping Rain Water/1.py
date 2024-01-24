from collections import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lefts = [0 for _ in range(n + 1)]
        rights = [0 for _ in range(n + 1)]

        # lefts부터 가장 높은 블럭 채우기
        for i in range(n - 1):
            lefts[i + 1] = max(lefts[i], height[i])
        
        # rights 채우기
        for i in range(n - 1, 0, -1):
            rights[i - 1] = max(rights[i], height[i])
        
        ans = 0

        for i in range(n):
            # 일단 양쪽 중 작은 곳을 구함.
            h = min(lefts[i], rights[i])

            # h랑 i번째 높이를 비교
            if h <= height[i]:
                continue

            ans += h - height[i]
        
        return ans
        