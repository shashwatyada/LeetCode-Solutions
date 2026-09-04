from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Step 1: Build adjacency list in-degree array
        adj = [[] for _ in range(numCourses)]
        in_degree = [0]* numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1

        # Step 2: Queue all courses with no prerequisites (in_degree == 0) 
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Step 3: Process BFS
        courses_taken = 0
        while queue:
            curr = queue.popleft()
            courses_taken += 1
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # If all courses could be processed, there were no cycles
        return courses_taken == numCourses