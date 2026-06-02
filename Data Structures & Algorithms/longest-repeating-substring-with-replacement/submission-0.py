class Solution: 
    def characterReplacement(self, s: str, k: int) -> int: 
        def kdiff(sub):
            if not sub: return True
            c = {}
            for i in sub:
                if i in c: c[i] += 1
                else: c[i] = 1

            max_freq = max(c.values())
            return (len(sub) - max_freq) <= k
            
        l, r = 0, 1
        c = 0
        while r <= len(s):
            if kdiff(s[l:r]):
                c = max(c, r - l)
                r += 1
            else:
                l += 1

        return c