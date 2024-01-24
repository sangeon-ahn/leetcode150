class Solution:
    def binToDec(self, binNum):
        res = 0
        mul = 1
        
        for idx, n in enumerate(binNum[::-1]):
            res += mul * int(n)
            mul *= 2
        
        return res

    def addBinary(self, a: str, b: str) -> str:
        sm = self.binToDec(a) + self.binToDec(b)
        print(sm)

        return bin(sm)[2:]

a = "1010"
b = "1011"

sol = Solution()
ans = sol.addBinary(a, b)
print(ans)