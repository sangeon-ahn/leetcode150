"""
    0idx부터 시작해서 이전 값이랑 1차이면 저장하고 다음꺼 보러 감
    1차이 아니면 정답에 지금까지 한거 추가하고 다시 시작지점 바꾸고 다시 시작
    
"""
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
            
        st = 0
        en = 1
        ans = []

        while en < len(nums):
            # nums[en]이 이전 값과 1차이면 en += 1
            if nums[en] - nums[en - 1] == 1:
                en += 1
            
            # 차이가 1보다 크면 답에 넣고 st 갱신
            else: 
                # st랑 en - 1이랑 같으면
                if st == en - 1:
                    ans.append(str(nums[st]))
                
                else:
                    temp = str(nums[st]) + "->" + str(nums[en - 1])
                    ans.append(temp)
                st = en
                en += 1
        
        # st에서 en까지 확인
        if st == en - 1:
            ans.append(str(nums[st]))
        else:
            ans.append(str(nums[st]) + "->" + str(nums[en - 1]))

        return ans        


        