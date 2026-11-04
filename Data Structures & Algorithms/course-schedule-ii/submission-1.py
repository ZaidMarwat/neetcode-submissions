class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []

        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        seen = set()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                res.append(i)
        
        while q:
            pre = q.popleft()
            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
                    res.append(course)
        
        return res if len(res) == numCourses else []
