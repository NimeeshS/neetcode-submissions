class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a = [0] * len(temperatures)
        l = []
        for i in range(len(temperatures)):
            while l and temperatures[l[-1]] < temperatures[i]:
                idx = l.pop()
                a[idx] = i - idx
            l.append(i)

        return a