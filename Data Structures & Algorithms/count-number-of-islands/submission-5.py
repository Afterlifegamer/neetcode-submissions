from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        is_checked = [[False for _ in range(cols)] for _ in range(rows)]
        def bfs(row,col):
            queue=deque()
            queue.append([row,col])
            if(is_checked[row][col]==False):
                is_checked[row][col]=True
            while queue:
                row,col=queue.popleft()
                if(row-1>=0 and is_checked[row-1][col]==False and grid[row-1][col]=="1"):
                    is_checked[row-1][col]=True
                    queue.append([row-1,col])
                if(row+1<rows and is_checked[row+1][col]==False and grid[row+1][col]=="1"):
                    is_checked[row+1][col]=True
                    queue.append([row+1,col])
                if(col-1>=0 and is_checked[row][col-1]==False and grid[row][col-1]=="1"):
                    is_checked[row][col-1]=True
                    queue.append([row,col-1])
                if(col+1<cols and is_checked[row][col+1]==False and grid[row][col+1]=="1"):
                    is_checked[row][col+1]=True
                    queue.append([row,col+1])
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(is_checked[i][j]==False and grid[i][j]=="1"):
                    
                    count+=1
                    bfs(i,j)
        return count




        
      


            
                


        


        