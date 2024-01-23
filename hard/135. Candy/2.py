"""
    <두번째 생각>
    [1, 2, 2, 2, 3, 2, 1, 1, 2, 3]
    :[1, 2, 1, 1, 2, 1, 0, -1, 0, 1]
    일단, 첫숫자는 1부터 시작해서 다음 숫자가 더 크면 현재값에 +1한 값을 준다.
    다음숫자가 더 작을 경우, 헬퍼함수를 수행하는데, 이 함수는 감소추세가 끝날 때까지 계속 배열을 순회하며 현재값에 -1한 값을 다음값으로 할당해준다.
    감소추세가 끝나는 지점에 도달했을 때, 마지막 감소한 숫자의 값을 확인 후, 0 이하인 경우 1과의 차이값만큼을 더해주는데, 범위는 감소추세가 시작된 가장 큰 숫자부터 더해준다.
    더해주면 해당 헬퍼함수가 끝나고, 이제 다시 감소추세가 끝난 숫자는 값을 이전 값보다 + 1 큰 값으로 시작한다.
    46/48에서 1052(오답) 1050(정답)으로 2차이나서 틀림
"""
from typing import List
class Solution:
    # curIdx는 맨 처음 인덱스
    def solve(self, curIdx, ratings, ans):
        # 감소가 끝날 때까지 계속 수행
        nextIdx = len(ratings)
        
        for i in range(curIdx + 1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                nextIdx = i
                break 
            

        """
        뒤에서부터 순회하면서 자기보다 크면 diff 더해주고,
        같으면 
        """
        ans[nextIdx - 1] = 1
        for i in range(nextIdx - 2, curIdx - 2, -1):
            if i < 0:
                break

            # i+1 == i면 i에 1 대입
            if ratings[i + 1] == ratings[i]:
                ans[i] = 1
            # i > i + 1 이면 i에 ans[i + 1] + 1 대입
            elif ratings[i] > ratings[i + 1]:
                ans[i] = ans[i + 1] + 1
            else:
                if ratings[i + 1] != ratings[i + 2]:
                    ans[i + 1] = max(ans[i], ans[i + 2]) + 1
                else:
                    ans[i + 1] = max(ans[i] + 1, ans[i + 2])
        
        return nextIdx

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [0 for _ in range(n)]
        ans[0] = 1
        
        idx = 1
        while idx < n:
            if ratings[idx - 1] < ratings[idx]:
                ans[idx] = ans[idx - 1] + 1
                idx += 1

            # 다음 숫자가 같거나 더 작을 경우
            else:
                nxtIdx = self.solve(idx - 1, ratings, ans) # 시작 인덱스, ratings 배열 넘겨주기, 다음 idx 반환 
                idx = nxtIdx
        print(ans)
        return sum(ans)

ratings = [1, 2, 3, 1, 2, 3, 3, 1]
sol = Solution()
ans = sol.candy(ratings)
print(ans)