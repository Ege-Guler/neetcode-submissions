from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-f for f in freq.values()]
        heapq.heapify(heap)
        time = 0

        cd = deque()


        while cd or heap:
            time += 1
            if heap:
                count = heapq.heappop(heap) + 1

                if count < 0:
                    cd.append((time + n, count))
            
            if cd and cd[0][0] == time:
                heapq.heappush(heap, cd.popleft()[1])
        
        return time
