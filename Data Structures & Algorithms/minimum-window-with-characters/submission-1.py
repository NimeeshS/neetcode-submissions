class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = {}
        for i in t:
            if i in dt:
                dt[i] += 1
            else:
                dt[i] = 1

        def check(s):
            d = {}
            for i in s:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

            for i in dt:
                if d.get(i, 0) < dt[i]: return False

            return True


        l, r = 0, len(t) - 1
        st = ""
        while r < len(s):
            if check(s[l:r+1]):
                if st == "" or len(s[l:r+1]) < len(st):
                    st = s[l:r+1]
                l += 1
            else:
                r += 1

        return st