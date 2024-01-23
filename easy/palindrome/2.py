class Solution:
    def convert(self, s: str) -> str:
        st, en = 0, len(s) - 1

        while st < en:
            while st < en and not s[st].isalnum():
                st += 1
            while st < en and not s[en].isalnum():
                en -= 1
            
            if s[st] != s[en]:
                return False
            st += 1
            en -= 1
        
        return True