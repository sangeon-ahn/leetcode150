"""
    1. 문제 분석
        정렬 안된 정수배열 nums
        가장 긴 연속적인 요소 순서 길이를 반환
        요구 시간복잡도: O(n)

        연속적 순열 => 1, 2, 3, 4 이런식으로 1씩 차이나는 순열
    
    2. 제약조건
        nums길이 <= 10만
        -10억 <= num <= 10억

    2. 풀이 방법
        - 정렬시 O(nlogn)이므로 정렬하면 안됨
        - 1. 공간복잡도 안좋은 풀이: num 최대, 최저 크기에 맞는 배열 생성 후 counting sort 방식으로 풀이
        - 2. 딕셔너리 사용 풀이
            - 키: 숫자, 값: true or false
            - 일단 nums 돌면서 딕셔너리에 저장한다.
            - nums 돌면서 각 숫자를 +, - 해가면서 dic에 있나 체크하며 길이값 갱신해나간다. 이때 방문한 숫자는 방문했다고 또 다른 딕셔너리에 체크 + cnt 변수 둬서 다 봤으면 중지
            - 시간복잡도: O(n + n + n)
        
"""
from typing import List
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic1 = defaultdict(bool)
        dic2 = defaultdict(bool)
        n = len(set(nums))
        # print(n)

        for num in nums:
            dic1[num] = True
        
        visits = 0
        maxLen = 0
        for num in nums:
            if visits == n:
                return maxLen

            if dic2[num]:
                continue

            dic2[num] = True

            tempNum = num + 1
            tempLen = 0

            while dic1[tempNum] and not dic2[tempNum]:
                dic2[tempNum] = True
                tempNum += 1
                tempLen += 1
            
            tempNum2 = num - 1
            tempLen2 = 0

            while dic1[tempNum2] and not dic2[tempNum2]:
                dic2[tempNum2] = True
                tempNum2 -= 1
                tempLen2 += 1
            
            maxLen = max(maxLen, tempLen + tempLen2 + 1)
            visits += (tempLen + tempLen2 + 1)
        
        return maxLen

nums = [1, 2, 0, 1]
sol = Solution()
ans = sol.longestConsecutive(nums)
            

        