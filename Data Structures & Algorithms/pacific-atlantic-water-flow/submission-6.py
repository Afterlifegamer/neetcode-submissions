from collections import deque
import copy
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific1=set()
        atlantic1=set()
        row=len(heights)
        col=len(heights[0])
        for i in range(row):
            for j in range(col):
                if(i==0):
                    if (i,j) not in pacific1:
                        pacific1.add((i,j))
                if(j==col-1):
                    if (i,j) not in atlantic1:
                        atlantic1.add((i,j))
                if(j==0):
                    if (i,j) not in pacific1:
                        pacific1.add((i,j))
                if i==row-1:
                    if (i,j) not in atlantic1:
                        atlantic1.add((i,j))
        pacific=copy.deepcopy(pacific1)
        atlantic=copy.deepcopy(atlantic1)
        def dfs(i,j,ocean):
            if(ocean=="P"):
                if(i-1>=0 and (i-1,j) not in pacific and heights[i-1][j]>=heights[i][j]):
                    pacific.add((i-1,j))
                    dfs(i-1,j,"P")
                if(i+1<row and (i+1,j) not in pacific and heights[i+1][j]>=heights[i][j]):
                    pacific.add((i+1,j))
                    dfs(i+1,j,"P")
                if(j-1>=0 and (i,j-1) not in pacific and heights[i][j-1]>=heights[i][j]):
                    pacific.add((i,j-1))
                    dfs(i,j-1,"P")
                if(j+1<col and (i,j+1) not in pacific and heights[i][j+1]>=heights[i][j]):
                    pacific.add((i,j+1))
                    dfs(i,j+1,"P")
            if(ocean=="A"):
                if(i-1>=0 and (i-1,j) not in atlantic and heights[i-1][j]>=heights[i][j]):
                    atlantic.add((i-1,j))
                    dfs(i-1,j,"A")
                if(i+1<row and (i+1,j) not in atlantic and heights[i+1][j]>=heights[i][j]):
                    atlantic.add((i+1,j))
                    dfs(i+1,j,"A")
                if(j-1>=0 and (i,j-1) not in atlantic and heights[i][j-1]>=heights[i][j]):
                    atlantic.add((i,j-1))
                    dfs(i,j-1,"A")
                if(j+1<col and (i,j+1) not in atlantic and heights[i][j+1]>=heights[i][j]):
                    atlantic.add((i,j+1))
                    dfs(i,j+1,"A")
            
        for i,j in pacific1:
            dfs(i,j,"P")
        for i,j in atlantic1:
            dfs(i,j,"A")
        output=[]
        for val in pacific:
            if(val in atlantic):
                i,j=val
                output.append([i,j])
        return(output)



        
       
                
                    
                    

        