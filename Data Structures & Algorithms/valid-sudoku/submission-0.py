class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            without = [i for i in row if i != "."]
            if len(set(without)) != len(without): return False
        for column in list(zip(*board)):
            without = [i for i in column if i != "."]
            if len(set(without)) != len(without): return False

        dir = [-1, 0, 1]

        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                without = [board[i+x][j+y] for x in dir for y in dir if board[i+x][j+y] != "."]
                if len(set(without)) != len(without): return False

        return True