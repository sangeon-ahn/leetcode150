from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = defaultdict(int)
        for ch in s:
            dic[ch] += 1
            
        for ch in t:
            if dic[ch] == 0:
                return False
            dic[ch] -= 1
        return True