class Solution:
    def convert(self, s: str) -> str:
        res = ""

        for ch in s:
            val = ord(ch)
            if 65 <= val <= 90:
                res += chr(val + 32)
            elif 97 <= val <= 122 or 48 <= val <= 57:
                res += ch
        return res

    def isPalindrome(self, s: str) -> bool:
        s = self.convert(s)
        n = len(s)
        if n <= 1:
            return True
        
        st = 0
        en = n - 1
        
        while st < en:
            if s[st] != s[en]:
                return False
            st += 1
            en -= 1
        
        return True