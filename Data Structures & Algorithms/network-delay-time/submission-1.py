from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        dist = {k: 0}
        heap = [(0, k)]

        while heap:

            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue
            
            for v, t in adj[u]:
                nd = d + t 
                if nd < dist.get(v, math.inf):
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        
        return max(dist.values()) if len(dist) == n else -1