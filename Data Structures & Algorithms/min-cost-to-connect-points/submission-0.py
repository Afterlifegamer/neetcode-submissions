class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        parent=list(range(n))
        size=[1]*n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            root_x,root_y=find(x),find(y)
            if(root_x==root_y):
                return False
            if(size[root_x]<size[root_y]):
                root_x,root_y=root_y,root_x
            size[root_x]+=size[root_y]
            parent[root_y]=root_x
            return True
        edges=[]
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                edges.append((abs(x1-x2)+abs(y1-y2),i,j))
        edges.sort()
        total_cost=0
        edge=0
        for cost,u,v in edges:
            if union(u,v):
                total_cost+=cost
                edge+=1
                if edge==n-1:
                    break
        return(total_cost)