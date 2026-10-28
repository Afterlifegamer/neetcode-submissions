from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(node):
            count=0
            q=deque()
            q.append(node)
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            while(q):
                count+=1
                for _ in range(len(q)):
                    i,j=q.popleft()
                    for rows,cols in directions:
                        if(i+rows in range(row) and j+cols in range(col) and grid[i+rows][j+cols]!=-1 and grid[i+rows][j+cols]!=0):
                            if(count<grid[i+rows][j+cols]):
                                grid[i+rows][j+cols]=count
                                q.append((i+rows,j+cols))

                                
                            

                   


                






        count=0
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if(grid[i][j]==0):
                    bfs((i,j))


        