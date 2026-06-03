import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            t = sum(math.ceil(i / mid) for i in piles)
            if t <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l