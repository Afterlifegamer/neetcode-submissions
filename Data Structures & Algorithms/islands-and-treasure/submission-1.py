from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        output=[]
        row=len(grid)
        col=len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==0):
                    output.append((i,j))
        queue=deque()
        for val in output:
            queue.append(val)
        while(queue):
            i,j=queue.popleft()
            count=grid[i][j]
            if(i-1>=0 and grid[i-1][j]>count+1):
                queue.append((i-1,j))
                grid[i-1][j]=count+1
            if(i+1<row and grid[i+1][j]>count+1):
                queue.append((i+1,j))
                grid[i+1][j]=count+1
            if(j-1>=0 and grid[i][j-1]>count+1):
                queue.append((i,j-1))
                grid[i][j-1]=count+1
            if(j+1<col and grid[i][j+1]>count+1):
                queue.append((i,j+1))
                grid[i][j+1]=count+1
        


        
                                
                            

                   


                






        