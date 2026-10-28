from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        count=0    
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        q=deque()
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==2):
                    q.append((i,j,0))
                elif(grid[i][j]==1):
                    fresh+=1
        minutes=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        while(q):
            i,j,time=q.popleft()
            minutes=max(minutes,time)
            for r,c in directions:
                row=r+i
                col=j+c
                if(row in range(rows) and col in range(cols) and grid[row][col]==1):
                    fresh-=1
                    grid[row][col]=2
                    q.append((row,col,time+1))
        return -1 if fresh>0 else minutes                   
                    

        

            

       
                    

        