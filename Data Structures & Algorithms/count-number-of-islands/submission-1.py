from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited=set()
        rows=len(grid)
        cols=len(grid[0])

        def bfs(r,c):
            count=0
            queue=deque()
            queue.append((r,c))
            print("This")
            while(queue):
                row,col=queue.popleft()
                visited.add((row,col))
                direction=[(0,1),(1,0),(-1,0),(0,-1)]
                for first,second in direction:
                    newr=row+first
                    newc=col+second
                    print("maybe")
                    if((newr,newc) not in visited and newr>=0 and newc>=0 and newr<rows and newc<cols and grid[newr][newc]=="1"):
                        print("This ran")
                        queue.append((newr,newc))
            
            return count+1
        count=0
        
        for r in range(rows):
            for c in range(cols):
                if((r,c) not in visited and grid[r][c]=="1"):
                    bfs(r,c)
                    count+=1
            
                    
        return count



            
                


        


        