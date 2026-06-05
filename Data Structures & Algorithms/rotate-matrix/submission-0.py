class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix1 = list(zip(*matrix[::-1]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix1[i][j]