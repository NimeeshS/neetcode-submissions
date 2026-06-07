class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(balance, s):
            if len(s) == 2 * n:
                if balance == 0:
                    res.append(s)
                return

            if balance < 0: return

            dfs(balance + 1, s + "(")
            dfs(balance - 1, s + ")")

        dfs(0, "")

        return res