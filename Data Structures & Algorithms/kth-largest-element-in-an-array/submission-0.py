class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        ans = 0
        for _ in range(k):
            ans = heapq.heappop(heap)

        return -ans