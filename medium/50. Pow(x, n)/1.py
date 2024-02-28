"""
    1. 문제 분석
        pow(x, n)값을 구해라.
        
        -100.0 < x < 100.0
        -2^31 <= n <= 2^31 - 1
        n은 정수
        x가 0이 아니거나 n > 0이다.
        -10^4 <= x^n <= 10^4

    2. 풀이 과정
        n이 매우 크기 때문에 분할정복 해야한다.
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(num, exp):
            if exp == 0:
                return 1
            if exp == 1:
                return num
            if exp == 2:
                return num**2
            
            val = pow(num, exp // 2)
            if exp % 2 == 0:
                return val * val
            
            else:
                return val * val * num
        
        if n < 0:
            if x < 0:
                if -n % 2 == 0:
                    return 1/pow(-x)
            if n % 2 == 0:
                return 1/pow(x, -n)
            return -1/pow(x, -n)
        else:
            return pow(x, n)

sol = Solution()
ans = sol.myPow(2.00000, -2)
print(ans)
                

            
        

        