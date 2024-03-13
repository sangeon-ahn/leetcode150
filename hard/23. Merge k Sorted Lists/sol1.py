class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []

        for l in lists:
            if l:
                # 정렬조건에 id(l)을 넣는 이유는 힙에 node 데이터 넣고싶은데 node는 정렬할 수 있는 값이 아니다. 따라서 무조건 다른 값인 id(l)을 넣어줌으로써 node들에 대해 정렬하려는 시도를 없앰으로써 node를 힙에 집어넣을 수 있도록 만든다.
                heapq.heappush(hq, (l.val, id(l), l))
        
        head = ListNode()
        temp = head

        while hq:
            _, _, node = heapq.heappop(hq)

            temp.next = node
            temp = temp.next

            if node.next:
                heapq.heappush(hq, (node.next.val, node.next))
        
        return head.next

            