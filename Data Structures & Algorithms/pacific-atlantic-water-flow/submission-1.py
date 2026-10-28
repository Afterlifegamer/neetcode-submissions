from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Rows=len(heights)
        Cols=len(heights[0])
        pac=[[False]*Cols for _ in range(Rows)]
        atl=[[False]*Cols for _ in range(Rows)]

        def bfs(source,ocean):
            q=deque(source)
            directions=[[0,1],[1,0],[0,-1],[-1,0]]
            while(q):
                r,c=q.popleft()
                ocean[r][c]=True
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if(row in range(Rows) and col in range(Cols) and heights[row][col]>=heights[r][c] and ocean[row][col]==False):
                        q.append((row,col))
    


        pacific=[]
        atlantic=[]

        for r in range(Rows):
            pacific.append((r,0))
            atlantic.append((r,Cols-1))
        for c in range(Cols):
            pacific.append((0,c))
            atlantic.append((Rows-1,c))
        bfs(pacific,pac)
        bfs(atlantic,atl)
        res=[]
        for r in range(Rows):
            for c in range(Cols):
                if(pac[r][c] and atl[r][c]):
                    res.append((r,c))

        return res
       
                
                    
                    

        