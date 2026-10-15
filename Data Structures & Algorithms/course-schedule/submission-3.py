class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            indegree[course] += 1
            adj[pre].append(course)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0
        visited = set()
        while q:
            course = q.popleft()
            if course in visited:
                return False
            visited.add(course)
            count += 1
            for post in adj[course]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    q.append(post)
                

        return count == numCourses


        





        print(indegree)
        print(adj)