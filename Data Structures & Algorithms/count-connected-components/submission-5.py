class Solution:
    from collections import defaultdict
    from collections import deque
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        dicts=defaultdict(list)
        queue=deque()
        def bfs(node):
            queue.append((node,None))
            while(queue):
                curr,parent=queue.popleft()
                visited.add(curr)
                for neighbours in dicts[curr]:
                    if(neighbours==parent or neighbours in visited):
                        continue
                    queue.append((neighbours,curr))
        for a,b in edges:
            dicts[a].append(b)
            dicts[b].append(a)
        count=0
        for node in range(n):
            if node not in visited:
                count+=1
                bfs(node)
        return count
        
        

        
        
                
                




        
            

        
        