from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u) 

        seen = set()

        def dfs(v, parent):
            
            seen.add(v)
            for next in adj[v]:
                # u-v, v-u
                if next == parent:
                    continue

                if next in seen:
                    return True

                if dfs(next, v):
                    return True
            
            return False
        
        if dfs(0, -1): # has cycle
            return False

        return len(seen) == n