from math import sqrt 
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidean(x):
            return sqrt((x[0]) ** 2 + (x[1]) ** 2)
        
        heap = []
        for point in points:
            distance = euclidean(point)

            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            elif len(heap) == k and -heap[0][0] > distance:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, point))

        return [p for d,p in heap]