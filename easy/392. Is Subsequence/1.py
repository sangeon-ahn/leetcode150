class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0

        for i in range(len(t)):
            if idx == len(s):
                return True
            if t[i] == s[idx]:
                idx += 1

        return False