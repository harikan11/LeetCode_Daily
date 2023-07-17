class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #for each course, make a list by mapping of its prereqs, this list is called adjacency list
        
        premap={ i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
            
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if premap[crs]==[]:
                return True
            
            visited.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            premap[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
        
                