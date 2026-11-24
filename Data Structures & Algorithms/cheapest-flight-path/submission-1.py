from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        INF = float("inf")

        dist = [INF] * n
        dist[src] = 0

        for _ in range(k + 1):
            new = dist[:]
            for u, v, p in flights:
                if dist[u] != INF and dist[u] + p < new[v]:
                    new[v] = dist[u] + p
            dist = new

        return dist[dst] if dist[dst] != INF else -1