"""
    1. 문제 분석
        n이 주어질 때, n!이 연속된 0으로 끝나면 그 0의 개수 
        0 <= n <= 1만

        시간복잡도 O(logN)으로 풀 수 있나요?

    2. 문제 풀이
        x * 10^y, x는 정수 꼴로 되어야 trailing zeros 존재
        10을 곱하면 0이 오른쪽에 추가됨
        10 = 2 * 5. 
        5 = 5 * 4 * 3 * 2 * 1, 5 1개 2 3개 -> 10 1개.
        
        200 = 17.x * 17.x, 17 = 1
        200 = 2 * 10^2 = 2^3 * 5^2 -> 2개
        
        n = 200이라면, 200 ~ 1 의 숫자들 중 2와 5로 나누어 떨어지는 횟수 구하면 된다.
        '2' ()'4' = 50 = 1 * 2 * 5 * 10 * 25 * 50) ('8' 1) 16 32 64 128 256 512 1024 2048 4096 8192
        5 25 125 625 3125 
        200 /5 = 40
        5: 1 2 3 4 5 6~ 40 -> 5 40개
        5: 8 -> 5^2 8개
        5: 1 -> 5^3 1개

        2: 1 ~ 100 -> 2 100개
        2: 1 ~ 50 -> 2^2 50개
        2: 1 ~ 25 -> 2^3 25개
        2: 1 ~ 12 -> 2^4 12개
        6
        3
        2^7 1개


        
        

"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        twos = 0
        fives = 0

        n1, n2 = n, n
        
        while n1 > 0:
            twos += n1 // 2
            n1 //= 2
        while n2 > 0:
            fives += n2 // 5
            n2 //= 5
        
        return min(twos, fives)


sol = Solution()
ans = sol.trailingZeroes(200)
print(ans)

        