class Solution:
    def myPow(self, x: float, n: int) -> float:
        p = 1
        e = abs(n)
        while e > 0:
            p *= x
            e -= 1

        return p if n > 0 else 1/p