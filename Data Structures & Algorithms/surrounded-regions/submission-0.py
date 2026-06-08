class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return
            if board[i][j] == "X" or board[i][j] == "T":
                return
            board[i][j] = "T"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"