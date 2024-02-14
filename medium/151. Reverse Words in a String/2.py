class Solution:
    def reverseWords(self, s: str) -> str:
        sLen = len(s)
        p = -1
        last = 0
        ans = ""
        for i in range(sLen):
            if s[i] != ' ':
                last = i
                break

        for i in range(sLen - 1, -1, -1):
            if p == -1 and s[i] != ' ':
                if last == i:
                    ans += s[i]
                    break
                p = i

            elif p != -1:
                if s[i] == ' ':
                    ans += s[i + 1:p + 1] + " "
                    p = -1
                elif last == i:
                    ans += s[i:p + 1]
                    break
        
        return ans