from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        queue=deque()
        dist = [float('inf')] * n
        dist[k-1]=0
        for u,v,t in times:
            if u not in graph:
                graph[u]=[(v,t)]
            else:
                graph[u].append((v,t))
        queue.append((k,0))
        while(queue):
            node,count=queue.popleft()
            for neigh,delay in graph[node]:
                if(delay+count<dist[neigh-1]):
                    dist[neigh-1]=delay+count
                    queue.append((neigh,delay+count))
        maxs=-1
        for val in dist:
            if(val==float('inf')):
                return -1
            if(val>maxs):
                maxs=val
        return maxs
                
        