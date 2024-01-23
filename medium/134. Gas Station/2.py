"""
    1. 문제 분석
    n개의 주유소가 있다.
    각 주유소는 gas[i]만큼의 가스가 있다.
    내 차는 i번째 주유소에서 i+1번째 주유소로 갈 때 cost[i]만큼 든다.
    아무 주유소에서든 출발할 수 있다.

    gas와 cost 리스트가 주어질 때, 시작 주유소 인덱스를 반환해라
    없으면 -1 반환해라.

    조건1: 시계방향으로 순환해서 다시 시작주유소로 돌아올 수 있는,
    조건2: 답이 있으면 해당 답이 유일하다.

    문제 이해 완료.
    그냥 gas for문 돌면서 더하고 빼다가 -나오면 break하고 다음거부터 시작하면?
    근데 중복된다? 
    2. 예시들
    [1, 2, 3, 4, 5], [3, 4, 5, 1, 2] -> gas[i], gas[i] - cost[i] + gas[i + 1]
    [-2, -2, -2, 3, 3] 이 중 양수에서만 시작 가능
    이렇게 시작 후보는 구했는데, 어디서 시작할지 어떻게 정함
    [3, -2, 0, 4, -9]면?



"""

from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        if n == 1:
            return 0

        vis = [False for _ in range(n)]

        for i in range(n):
            if vis[i]:
                continue

            vis[i] = True
            
            # 우선, i주유소에 방문한거부터 시작.
            idx = i % n
            tempTotalGas = 0

            # 해당 주유소 방문 -> 다음 주유소 넘어가기
            while True:
                tempTotalGas += gas[idx] # 현재 주유소 충전
                tempTotalGas -= cost[idx] # 다음 주유소로 이동

                # 이동 못할시
                if tempTotalGas < 0:
                    # 다음 주유소를 시작위치로 잡음
                    break

                # 이동 할 수 있을 시,
                else:
                    # 현재 주유소 방문체크하기
                    vis[idx] = True
                    idx = (idx + 1) % n # 다음 주유소 위치

                    # 다음 위치가 원래의 나라면 순환 가능
                    if idx == i:
                        return i
        
        # for문 다 돌았는데 안끝나면 -1 리턴
        return -1
                
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

sol = Solution()
ans = sol.canCompleteCircuit(gas, cost)
print(ans)