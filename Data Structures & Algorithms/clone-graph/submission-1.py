"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew={}
        def bfs(node):
            q=deque()
            q.append(node)
            
            while q:
                node=q.popleft()
                if node not in oldToNew:
                    copy=Node(node.val)
                    oldToNew[node]=copy
                else:
                    copy=oldToNew[node]
                for nei in node.neighbors:
                    if nei not in oldToNew:
                        new=Node(nei.val)
                        oldToNew[nei]=new
                        copy.neighbors.append(new)
                        q.append(nei)
                    else:
                        copy.neighbors.append(oldToNew[nei])
        bfs(node)
                

                   
        return oldToNew[node] if node else None

        
        