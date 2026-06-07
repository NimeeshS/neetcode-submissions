class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, part):
            if i == len(s):
                res.append(part[:])
                return

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    part.append(s[i:j+1])
                    dfs(j + 1, part)
                    part.pop()

        dfs(0, [])
        return res