class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            if task in counts: counts[task] += 1
            else: counts[task] = 1

        heap = []
        for task in counts:
            heapq.heappush(heap, -counts[task])
        q = []
        time = 0

        while heap or q:
            if heap:
                task = heapq.heappop(heap)
                if task < -1:
                    q.append([task + 1, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.pop(0)[0])
            time += 1

        return time