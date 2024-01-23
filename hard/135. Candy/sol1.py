from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n 

        # 일단 한번 쫙 돌면서 이전값이 더 작은 경우에 이전값 + 1로 초기화해줌
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # 이후, 뒤에서부터 역순으로 돌면서 기존 값이랑 다음 값 + 1이랑 비교해서 더 큰 값으로 해줌. 이유: 첫번째 for문으로 만들어진 값은 자신의 이전 값을 고려한 답 후보이고, 뒤에서부터 돌면서 이제 뒤에 숫자까지 고려한 답을 도출해내기 위해 앞숫자 + 뒷숫자 전부를 수용할 수 있는 값인 둘 중 더 큰 값을 답으로 하는 것이다.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        return sum(candies)

sol = Solution()
ans = sol.candy([1, 1, 2])
print(ans)