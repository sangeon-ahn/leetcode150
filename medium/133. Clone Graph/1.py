"""
    방향 없는 연결된 그래프가 주어질 때, 해당 그래프의 deep copy를 반환하라.
    각 노드의 val은 각 노드의 번호와 동일하다.
    근데 인자로 번호가 1인 node 하나만 들어온다. 따라서 타고타고 들어가면서 푸는게 정석
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # 생성된 노드 저장리스트 만들기
        created = [None for _ in range(101)]
        connected = set()

        # bfs로 풀기
        q = deque()
        head = Node(1)
        created[head.val] = head
        q.append([node, head])

        while q:
            origin, copied = q.popleft()

            for nxt in origin.neighbors:
                if (origin.val, nxt.val) not in connected:
                    # 아직 생성 안된거면 생성해서 넣기
                    if created[nxt.val] is None:
                        nxtNode = Node(nxt.val)
                        created[nxt.val] = nxtNode
                        q.append([nxt, nxtNode])
                        
                    # 연결
                    copied.neighbors.append(created[nxt.val])
                    created[nxt.val].neighbors.append(copied)

                    connected.add((origin.val, nxt.val))
                    connected.add((nxt.val, origin.val))

        return head

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors.append(n2)
n1.neighbors.append(n4)

n2.neighbors.append(n1)
n2.neighbors.append(n3)

n3.neighbors.append(n2)
n3.neighbors.append(n4)

n4.neighbors.append(n1)
n4.neighbors.append(n3)
                    
sol = Solution()
ans = sol.cloneGraph(n1)

                


            

        