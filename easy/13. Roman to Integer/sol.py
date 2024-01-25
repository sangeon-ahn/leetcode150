"""
    로마자 표기법은 일반적인 경우 오른쪽으로 갈수록 더 작은 숫자가 배치된다.
    하지만, 오른쪽 숫자가 더 큰 숫자인 경우, 두 기호의 조합이 이루어진다.
    따라서 위 경우에 현재값 - 이전값 * 2를 더해주면 바로 직전에 더해진 값을 추가하면,
    (현재값 - 이전값)이 더해지게 된다.
"""
class Solution:
    def romanToInt(self, s: str) -> int:

        lookup = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 00, "D" : 500, "M" : 1000}
        
        prev = None
        sum = 0

        for ch in s:
            current = lookup[ch]
            if prev == None:
                sum += current
            else:
                if current > prev:
                    sum +=  current - prev * 2
                else:
                    sum += current
            prev = current
        return sum     
        