class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = 0
        n = len(s)
        idx = 0

        while idx < n:
            if s[idx] == 'I':
                if idx + 1 < n and s[idx + 1] == 'V':
                    idx += 1
                    ans += 4
                elif idx + 1 < n and s[idx + 1] == 'X':
                    idx += 1
                    ans += 9
                else:
                    ans += dic[s[idx]]
            
            elif s[idx] == 'X':
                if idx + 1 < n and s[idx + 1] == 'L':
                    idx += 1
                    ans += 40
                elif idx + 1 < n and s[idx + 1] == 'C':
                    idx += 1
                    ans += 90
                else:
                    ans += dic[s[idx]]
            
            elif s[idx] == 'C':
                if idx + 1 < n and s[idx + 1] == 'D':
                    idx += 1
                    ans += 400
                elif idx + 1 < n and s[idx + 1] == 'M':
                    idx += 1
                    ans += 900
                else:
                    ans += dic[s[idx]]
            else:
                ans += dic[s[idx]]
            idx += 1

        return ans