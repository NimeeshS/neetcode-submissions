class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        d1 = {}
        for i in s1:
            if i in d1: d1[i] += 1
            else: d1[i] = 1
        for i in range(len(s1) - 1, len(s2)):
            d2 = {}
            for j in s2[i-len(s1)+1:i+1]:
                if j in d2:
                    d2[j] += 1
                    if d2[j] > d1[j]: break
                else:
                    if j not in d1: break
                    d2[j] = 1

            if d1 == d2: return True

        return False