# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        node = head
        while node is not None:
            if node not in visited:
                visited.add(node)
                node = node.next
            
            else:
                return True
        return False

        