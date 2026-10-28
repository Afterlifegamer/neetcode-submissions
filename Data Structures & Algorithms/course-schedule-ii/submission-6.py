class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preq[crs].append(pre)

        visited=set()
        curr=[]
        result=set()
        def dfs(crs):
            if(crs in visited):
                return False
            if(crs in result):
                return True
            if(preq[crs]==[]):
                curr.append(crs)
                result.add(crs)
                return True
            
            visited.add(crs)
            
            for prequi in preq[crs]:
                if not dfs(prequi):
                    
                    return False
            curr.append(crs)
            visited.remove(crs)
            result.add(crs)
            preq[crs]=[]
            return True
        for crs in range(numCourses):
            if crs not in result:
                if not dfs(crs):
                    return []
        return curr
        