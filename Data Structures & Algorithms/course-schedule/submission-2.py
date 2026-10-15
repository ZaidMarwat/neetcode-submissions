class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        m = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            m[course].append(pre)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not m[course]:
                return True

            visited.add(course)
            for pre in m[course]:
                if not dfs(pre):
                    return False
            m[course] = []
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False


        return True
                
