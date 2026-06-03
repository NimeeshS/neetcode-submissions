class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        for i in range(len(matrix)):
            if matrix[i][l] <= target <= matrix[i][r]:
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] < target:
                        l = mid + 1
                    elif matrix[i][mid] > target:
                        r = mid - 1
                    else:
                        return True

        return False