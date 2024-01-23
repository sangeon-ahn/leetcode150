from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        tank = idx = 0

        # 이렇게 하면 되는 이유?
        # tank값이 음수일 때만 idx가 다음 주유소로 갱신되고, 이후에 양수가 지속되다가 음수가 나오면 그 구간에서 시작은 불가능하므로 다음 지점 가리킴
        #근데 음수-음수 나오고, 마지막 인덱스일 경우가 있나? -> 없다. 이미 -1 리턴하는 조건을 통과한 것이기 때문에 무조건 답이 있어야 한다.
        # 따라서 +++만 계속되면 +가 시작하는 맨 처음이 시작점인게 가장 가능성이 높은것이므로 i+1을 답으로 하면 됨.
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        
        return idx