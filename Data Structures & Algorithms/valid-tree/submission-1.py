class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        preq={i:[] for i in range(n)}
        for crs,pre in edges:
            preq[crs].append(pre)
            preq[pre].append(crs)
            
        if(len(edges)!=n-1):
            return False
        visited=set()
        def dfs(crs,parent):
            
                
            if(crs in visited):
                return False
            
            if(preq[crs]==[]):
                visited.add(crs)
                return True
            visited.add(crs)
            
            for prequi in preq[crs]:
                if(prequi==parent):
                    continue
                if not dfs(prequi,crs):
                    return False
            
            
            preq[crs]=[]
            return True
        res=dfs(0,-1)
        return len(visited)==n
        