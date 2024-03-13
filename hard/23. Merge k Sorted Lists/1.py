# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional
"""
    오름차순 정렬된 리스드들이 주어질 때, 하나의 오름차순 링크드리스트로 만들어라.
    lists의 요소는 각 링크드리스트의 head Node이다.
    리스트들 head 가리키는 포인터 생성후 배열에 넣고
    한 턴마다 제일 작은게 채택되고 다음 노드로 향하는 방식
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        pointers = []
        for l in lists:
            temp = l
            pointers.append(temp)
        

        head = ListNode() 

        temp = head
        while True:
            # 일단, pointers에서 꺼내서 값 확인하고 젤 작은 노드가 head.next가 됨
            minVal = float('inf')
            minNode = None
            pos = 0

            for idx, p in enumerate(pointers):
                if p and p.val < minVal:
                    minNode = p
                    minVal = p.val
                    pos = idx
            
            # 노드가 다 None이면 끝
            if minVal == float('inf'):
                break
            

            pointers[pos] = pointers[pos].next

            # 그 외엔 이어붙이기
            temp.next = minNode
            temp = temp.next
            
        return head.next
            

            
            

        
        
        
        
            

        