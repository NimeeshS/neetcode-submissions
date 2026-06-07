class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if k == len(word):
                return True

            if (i, j) in visited or not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return False

            if board[i][j] != word[k]:
                return False

            visited.add((i, j))
            result =  (
                dfs(i + 1, j, k + 1) or
                dfs(i - 1, j, k + 1) or
                dfs(i, j + 1, k + 1) or
                dfs(i, j - 1, k + 1)
            )
            visited.remove((i, j))
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, 0): return True

        return False