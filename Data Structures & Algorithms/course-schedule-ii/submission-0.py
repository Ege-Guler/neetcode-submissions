from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        in_degrees = [0] * numCourses

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degrees[course] += 1

        order = [-1] * numCourses
        index = 0
        
        # v          0 1 2 3
        # in degree [0 1 4 0]
        q = deque([ix for ix in range(numCourses) if in_degrees[ix] == 0])

        while q:

            v = q.popleft()

            order[index] = v
            index += 1

            for nxt in adj[v]:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    q.append(nxt)
            
        return order if index == numCourses else []


