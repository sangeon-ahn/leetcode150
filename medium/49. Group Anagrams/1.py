"""
    1. 문제 분석
        단어들이 주어질 때, 아나그램 그룹으로 분류해서 리턴하라.

        아나그램: 문자를 재졍렬해서 해당 단어를 만들 수 있는 단어들

        단어 개수 <= 10000
        단어 길이 <= 100
    
    2. 풀이 방법
         - 각 단어를 정렬한다.
         - 정렬된 단어를 키로, 리스트를 값으로 한 후 값에 단어를 넣는다.
         - 전부 수행한 후, 딕셔너리 순회하며 반환.

"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            dic[''.join(sorted(word))].append(word)
        
        ans = []
        for x in dic.values():
            ans.append(x)

        return ans


strs = ["eat","tea","tan","ate","nat","bat"]
sol = Solution()
ans = sol.groupAnagrams(strs)


        