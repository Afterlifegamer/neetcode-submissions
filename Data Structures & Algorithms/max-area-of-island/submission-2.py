class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(r,c):
            count=1
            q=deque()
            visited.add((r,c))
            q.append((r,c))
            while(q):
                row,column=q.popleft()
                directions=[[0,1],[1,0],[-1,0],[0,-1]]
                for dr,dc in directions:
                    r,c=row+dr,column+dc
                    if(r in range(rows)and c in range(cols)and grid[r][c]==1 and (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
                        count+=1
                        
                    
            return count

        
        count=0
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        maxarea=0
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==1 and (r,c) not in visited):
                    
                    
                    area=bfs(r,c)
                    
                    maxarea=max(maxarea,area)
        
        return maxarea
        