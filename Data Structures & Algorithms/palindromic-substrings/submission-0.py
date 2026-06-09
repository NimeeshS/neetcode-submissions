class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        def check(i, j):
            nonlocal c
            while i >= 0 and j < len(s) and s[i] == s[j]:
                c += 1
                i -= 1
                j += 1
            
        for i in range(len(s)):
            check(i, i)
            check(i, i + 1)

        return c