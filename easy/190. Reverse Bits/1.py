class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        idx = 0

        while idx < 32: 
            # n을 2로 나눈 나머지 구함
            div = n % 2
            n >>= 1

            # div가 0이면 1로 치환하고 계산
            if div == 1:
                ans += 2**(31 - idx)

            idx += 1
        
        return ans

n = 43261596
sol = Solution()
ans = sol.reverseBits(n)
