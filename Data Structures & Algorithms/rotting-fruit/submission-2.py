from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if(grid[i][j]==2):
                    queue.append((i,j))
                    
        count=2
        while(queue):
            count+=1
            for k in range(len(queue)):
                i,j=queue.popleft()
                if(i-1>=0 and grid[i-1][j]==1):
                    queue.append((i-1,j))
                    grid[i-1][j]=count
                if(i+1<row and grid[i+1][j]==1):
                    queue.append((i+1,j))
                    grid[i+1][j]=count
                if(j-1>=0 and grid[i][j-1]==1):
                    queue.append((i,j-1))
                    grid[i][j-1]=count
                if(j+1<col and grid[i][j+1]==1):
                    queue.append((i,j+1))
                    grid[i][j+1]=count
        for i in range(row):
            for j in range(col):
                if(grid[i][j]==1):
                    return -1
        if(count==2):
            return 0
        return count-3



                    
            

                         
                    

        

            

       
                    

        