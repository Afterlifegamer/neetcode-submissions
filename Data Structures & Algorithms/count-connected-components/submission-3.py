class Solution:
    from collections import defaultdict
    from collections import deque
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        dicts=defaultdict(list)
        def bfs(node):
            queue=deque()
            queue.append(node)
            visited.add(node)
            while(queue):
                curr=queue.popleft()
                for neighbour in dicts[curr]:
                    if(neighbour not in visited):
                        visited.add(neighbour)
                        queue.append(neighbour)
        
        for left,right in edges:
            dicts[left].append(right)
            dicts[right].append(left)
        res=0
        for node in range(n):
            if node not in visited:
                
                bfs(node)
                res+=1
        return res

        
                
                




        
            

        
        