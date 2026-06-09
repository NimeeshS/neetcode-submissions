class Solution:
    def longestPalindrome(self, s: str) -> str:
        st = ""
        def check(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        for i in range(len(s)):
            c = check(i, i)
            if len(c) > len(st): st = c
            c = check(i, i + 1)
            if len(c) > len(st): st = c

        return st