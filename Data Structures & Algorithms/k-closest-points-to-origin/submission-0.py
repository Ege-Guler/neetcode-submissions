from math import sqrt
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        heap = []
        for point in points:
            heapq.heappush(heap, (-self.euclidean_distance_to_origin(point), point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for _, point in heap]

    def euclidean_distance_to_origin(self, point: List[int]) -> float:
        return sqrt(pow((point[0]), 2) +  pow((point[1]), 2))

        