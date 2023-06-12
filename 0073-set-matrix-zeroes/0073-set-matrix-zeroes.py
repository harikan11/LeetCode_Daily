class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_rows, zero_cols = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        for i in zero_rows:
            matrix[i] = [0] * len(matrix[0])
        for j in zero_cols:
            for i in range(len(matrix)):
                matrix[i][j] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        