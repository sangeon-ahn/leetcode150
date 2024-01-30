"""
    1차원 dp 배열을 안씀으로써 공간복잡도 O(N) -> O(1) 풀이 방법
"""

class Solution(object):
    def rob(self, nums):
        rob, noRob = 0, 0

        for num in nums:
            newRob = noRob + num # 훔친 경우: num을 더함.
            newNoRob = max(noRob, rob) # 안 훔친 경우: 그냥 기존 두 값중 더 큰값을 취함.
            rob, noRob = newRob, newNoRob # 다시 갱신
        
        return max(rob, noRob) # 가장 마지막 단계에서의 훔친 경우, 안 훔친 경우중 더 큰 값을 반환