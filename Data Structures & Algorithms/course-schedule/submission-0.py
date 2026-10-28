class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preq[crs].append(pre)

        visited=set()
        def dfs(crs):
            if(crs in visited):
                return False
            if(preq[crs]==[]):
                return True
            visited.add(crs)
            for prequi in preq[crs]:
                if not dfs(prequi):
                    return False
            visited.remove(crs)
            preq[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True