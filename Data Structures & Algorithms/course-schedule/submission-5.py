class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # store all indegrees per course
        # store adjacency lists per course
        # both at index of course
        # append to queue courses with no in degrees
        # go through bfs removing first course in queue and in degrees of adjacent courses
        # if in degree is 0 append to queue

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
        while q:
            course = q.popleft()
            count += 1
            for post in adj[course]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    q.append(post)
                

        return count == numCourses