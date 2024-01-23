from typing import List;
"""
    감소하지 않는 배열 nums가 있을 때, 배열에 속해 있는 각각의 수들이 최대 2개씩만 있도록 배열을 만들기. 새롭게 배열 만들면 안되고 해당 nums를 반환해야 함.
    다른 배열 할당해서 풀지 마시오. 

    풀이법: 일단, nums의 첫, 두번째 요소까지는 그냥 넣어도 된다. 만약 두 수가 같다고 하더라도 2개이기 때문에 조건을 만족한다.
    3개 이후부터는 (해당 인덱스 - 2)번째의 수가 자신과 같은지 같지 않은지 파악한다.
    같다면 무시하고 다음 수를 보러가고 다르다면 추가한다.
    외부 포인터를 만들어야 한다. 이 포인터는 지금 값을 추가해야 할 위치를 알려준다.
    이후 for문을 돌면서 넣어도 되는지를 조건에 따라 판별한다.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        
        p = 2

        for i in range(2, len(nums)):
            if nums[p - 2] != nums[i]:
                nums[p] = nums[i]
                p += 1

nums = [1, 1, 1, 2, 2, 3]
sol = Solution()
ans = sol.removeDuplicates(nums)

print(ans)
print(nums)