class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        l = [0] * n
        l[0] = 1
        l[1] = 2
        for i in range(2, n):
            l[i] = l[i - 2] + l[i - 1]

        return l[-1]