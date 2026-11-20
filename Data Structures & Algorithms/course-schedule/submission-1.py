from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses=defaultdict(list)
        path=set()
        visited=set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            path.add(course)
            for next_course in courses[course]:
                if not dfs(next_course):
                    return False
            path.remove(course)
            visited.add(course)
            return True


            
        
        for a,b in prerequisites:
            courses[b].append(a)
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    
        
        