from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        in_degrees = [0] * numCourses

        for post, pre in prerequisites:
            adj[post].append(pre)
            in_degrees[pre] += 1

        index = 0

        q = deque([ix for ix, start in enumerate(in_degrees) if start == 0])

        while q:
            v = q.popleft()

            # decrease in degree since parent is removed
            for nxt in adj[v]:
                in_degrees[nxt] -= 1
                if in_degrees[nxt] == 0:
                    q.append(nxt)
            index += 1

        return index == numCourses