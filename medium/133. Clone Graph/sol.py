# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visitedMap = {}

        def clone(node):
            if not node:
                return node
            
            if node in visitedMap:
                return visitedMap[node]
            
            cloneNode = Node(node.val, [])
            visitedMap[node] = cloneNode

            for nbr in node.neighbors:
                cloneNode.neighbors.append(clone(nbr))
            
            return cloneNode
        
        return clone(node)