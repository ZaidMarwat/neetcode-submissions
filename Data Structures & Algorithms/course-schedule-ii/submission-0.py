class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegrees = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegrees[course] += 1
            adj[pre].append(course)
        
        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        
        count = 0
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            count += 1
            for post in adj[course]:
                indegrees[post] -= 1
                if indegrees[post] == 0:
                    q.append(post)
        return res if count == numCourses else []
