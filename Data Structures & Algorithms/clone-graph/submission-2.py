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
        queue=deque()
        result=[]
        hashmap={}
        def bfs(node):
            queue.append(node)
            hashmap[node]=Node(node.val)
            while(queue):
                output=[]
                root=queue.popleft()
                for nodes in root.neighbors:
                    
                    if(nodes not in hashmap):
                        hashmap[nodes]=Node(nodes.val)
                        queue.append(nodes)
                    hashmap[root].neighbors.append(hashmap[nodes])
                    
                    
        if not node:
            return None        
        bfs(node)
        return(hashmap[node])



        
            
       

        
        