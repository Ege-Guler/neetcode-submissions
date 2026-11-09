from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        seen = set()
        comp_count = 0

        for i in range(n):

            if i in seen: 
                continue

            q = deque([i])
            seen.add(i)
            while q:
                v = q.popleft()

                for nxt in adj[v]:
                    if nxt not in seen:
                        q.append(nxt)
                        seen.add(nxt)

            comp_count += 1
        
        return comp_count