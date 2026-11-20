from collections import deque
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph=defaultdict(list)
        if(n!=len(edges)+1):
            return False
        else:
            visited=set()
            queue=deque()
            for a,b in edges:
                graph[a].append(b)
                graph[b].append(a)
            queue.append((0,0))
            count=0
            while(queue):
                count+=1
                prev,node=queue.popleft()
                if(node in visited):
                    return False
                visited.add(node)
                for nodes in graph[node]:
                    if(nodes!=prev):
                        queue.append((node,nodes))
            print(count)
            if(count<n):
                return False
            return True
            

            
       
        