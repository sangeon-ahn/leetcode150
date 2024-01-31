"""
    일단, 아무 생각없이 3중 for문으로 풀면 O(N^3)임. 
    근데 왜 오름차순 정렬하고 왼쪽에서부터 숫자 하나 선택하고 나머지 부분에 대해 투포인터로 좁혀가면서 찾으면 되는데 이건 O(N^2)임
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.append(-float('inf'))
        # nums를 오름차순 정렬
        nums.sort()

        # nums를 순회함.
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            # 나머지 구간에 대해 투포인터 생성
            st = i + 1
            en = len(nums) - 1
            
            target = -nums[i]

            # while 돌면서 합이 target값과 같은지 확인
            while st < en:
                temp = nums[st] + nums[en]
                # target값과 같으면,

                if temp == target and (nums[i], nums[st], nums[en]) not in ans:
                    ans.append((nums[i], nums[st], nums[en]))
                    st += 1
                    en -= 1
                
                # target보다 크면,
                elif temp > target:
                    # en을 낮춤
                    en -= 1
                
                # target보다 작으면,
                else:
                    # st를 높임
                    st += 1
        
        return list(map(list, ans))



        