# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional 
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 링크드리스트 값 뽑아내기
        values = []
        
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        # 2. 값 정렬하기
        values.sort()

        # 3. 정렬된 값 할당하기
        node = head
        idx = 0
        while node:
            node.val = values[idx]
            node, idx = node.next, idx + 1
        
        return head
        