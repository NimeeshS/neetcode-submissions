class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, posDiag, negDiag = set(), set(), set()

        def dfs(i, board):
            if i == n:
                res.append(["".join(i) for i in board])
                return

            for j in range(n):
                if j in cols or i+j in posDiag or i-j in negDiag:
                    continue
                else:
                    cols.add(j)
                    posDiag.add(i + j)
                    negDiag.add(i - j)
                    board[i][j] = "Q"
                    dfs(i + 1, board)
                    board[i][j] = "."
                    cols.remove(j)
                    posDiag.remove(i + j)
                    negDiag.remove(i - j)

        dfs(0, [["." for _ in range(n)] for _ in range(n)])
        return res