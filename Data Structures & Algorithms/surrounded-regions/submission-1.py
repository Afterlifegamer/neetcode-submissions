from collections import deque
class Solution:
    def solve(self, heights: List[List[str]]) -> None:
        visited=set()
        row=len(heights)
        col=len(heights[0])
        queue=deque()
        for i in range(row):
            for j in range(col):
                if((i==0 or i==row-1) and heights[i][j]=='O'):
                    queue.append((i,j))
                    visited.add((i,j))
                elif((j==0 or j==col-1) and heights[i][j]=='O'):
                    queue.append((i,j))
                    visited.add((i,j))
        while(queue):
            i,j=queue.popleft()
            if(i-1>=0 and (i-1,j) not in visited and heights[i-1][j]=='O'):
                queue.append((i-1,j))
                visited.add((i-1,j))
            if(i+1<row and (i+1,j) not in visited and heights[i+1][j]=='O'):
                queue.append((i+1,j))
                visited.add((i+1,j))
            if(j-1>=0 and (i,j-1)not in visited and heights[i][j-1]=='O'):
                queue.append((i,j-1))
                visited.add((i,j-1))
            if(j+1<col and (i,j+1) not in visited and heights[i][j+1]=='O'):
                queue.append((i,j+1))
                visited.add((i,j+1))
        for i in range(row):
            for j in range(col):
                if(heights[i][j]=='O'and (i,j) not in visited ):
                    heights[i][j]='X'




        