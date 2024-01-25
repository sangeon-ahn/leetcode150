"""
    투 포인터 문제.
    오름차순 정렬되어 있으므로, st, en 포인터 각각 만들어서 조이다가 타겟값과 합이 같을 때 리턴하면 된다.
"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = 0
        en = len(numbers) - 1

        while st < en:
            val = numbers[st] + numbers[en]
            if val == target:
                return [st + 1, en + 1]
            
            elif val > target:
                en -= 1
            else:
                st += 1 

        return [0, 0]

        