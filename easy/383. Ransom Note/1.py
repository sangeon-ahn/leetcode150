from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = defaultdict(int)

        for ch in magazine:
            dic[ch] += 1
        
        for ch in ransomNote:
            if ch not in dic:
                return False
            
            if dic[ch] == 0:
                return False

            dic[ch] -= 1
        
        return True

sol = Solution()
ans = sol.canConstruct()

        