from typing import List
"""
    시복O(N), 공간복잡도 O(1)에 풀기 위해서는 약간의 변수 선언과 for문만 돌아서 풀어야 한다. -> 모르겠다.
    가장 쉽게 떠오르는 풀이는 딕셔너리를 만든 후, nums for문 돌면서 하나씩 세준 후, 딕셔너리 순회하면서 값이 n/2인 key를 답으로 하는 것.
    시복: O(N), 공복: O(K), K: 유니크 정수의 개수

    
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()

        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        
        major = len(nums) / 2
        ans = 0
        for n in dic.keys():
            if dic[n] > major:
                ans = n
                break
        
        return ans

        
            
            
        