import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        # 1 2 3 4 5 
        # 5 4
        #
        for num in nums:

            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]