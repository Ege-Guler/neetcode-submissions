import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_counter = {}
        for task in tasks:
            task_counter[task] = task_counter.get(task, 0) + 1

        heap = [-c for c in task_counter.values()]
        heapq.heapify(heap)

        queue = deque()

        time = 0

        while heap or queue:
            time += 1
            
            if heap:
                count = heapq.heappop(heap) + 1 # max heap neg
                if count != 0:
                    # when available
                    queue.append((count, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time


        