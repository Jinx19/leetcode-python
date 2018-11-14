class Solution:
    def find(self, matrix, rows, columns, target):
        """
        :type matrix: [[]]
        :type rows: int
        :type columns: int
        :type target: int
        :rtype: bool
        """
        row, col = 0, columns - 1

        while row >= 0 and row < rows and col >= 0 and col < columns:
            if target == matrix[row][col]:
                return True
            else:
                if target > matrix[row][col]:
                    row += 1
                else:
                    col -= 1
        return False
