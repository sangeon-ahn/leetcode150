from typing import List
"""
    n <= 10만
    그냥 dfs 돌려보자.
    vis 배열 만든 후, 방문시 체크
    모든 도시 방문시, 자기 자신으로 갈 수 있으면 retrun 초기위치 리턴
    중간에 -시 패스
"""
Cost = []
Gas = []
Vis = []
Answer = -1
class Solution:
    def dfs(self, initPos, curPos, curGas, visCnts, n):
        global Answer, Vis, Gas, Cost
        if visCnts == n:
            if Cost[curPos] > curGas:
                return
            else:
                Answer = initPos
                return
        
        for i in range(n):
            if Vis[i]:
                continue

            if curGas + Gas[i] < Cost[i]:
                continue

            Vis[i] = True
            self.dfs(initPos, i, curGas + Gas[i] - Cost[i], visCnts + 1, n)
            Vis[i] = False
                

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        global Cost, Gas, Vis
        Cost = cost
        Gas = gas
        Vis = [False for _ in range(len(gas))]

        for i in range(len(gas)):
            if Answer != -1:
                break

            Vis[i] = True
            self.dfs(i, i, 0, 1, len(gas))
            Vis[i] = [False for _ in range(len(gas))]
        
        return Answer

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
sol = Solution()
ans = sol.canCompleteCircuit(gas, cost)
print(ans)
        