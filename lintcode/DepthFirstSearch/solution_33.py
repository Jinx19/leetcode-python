# N queen problem


# 1) Start in the leftmost column
# 2) If all queens are placed
#     return true
# 3) Try all rows in the current column.  Do following for every tried row.
#     a) If the queen can be placed safely in this row then mark this [row,
#         column] as part of the solution and recursively check if placing queen here leads to a solution.
#     b) If placing the queen in [row, column] leads to a solution then return
#         true.
#     c) If placing queen doesn't lead to a solution then umark this [row,
#         column] (Backtrack) and go to step (a) to try other rows.
# 3) If all rows have been tried and nothing worked, return false to trigger
#     backtracking.
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def isSafe(self, plane, row, col, n):

        for i in range(col):
            if plane[row][i] == 'Q':
                return False

        left = col - 1
        top = row - 1
        while left > -1 and top > -1:
            if plane[top][left] == 'Q':
                return False
            left = left - 1
            top = top - 1

        left = col - 1
        low = row + 1
        while left > -1 and low < n:
            if plane[low][left] == 'Q':
                return False
            left = left - 1
            low = low + 1

        return True

    def dfs(self, plane, col, n, result):
        if col == n:
            result.append(["".join(plane[i]) for i in range(n)])
            for x in range(n):
                plane[x][col - 1] = '.'
            return True
        for row in range(n):

            isSafe = self.isSafe(plane, row, col, n)
            if isSafe:
                plane[row][col] = 'Q'
                if not self.dfs(plane, col + 1, n, result):
                    plane[row][col] = '.'

        return False

    def solveNQueens(self, n):
        # write your code here
        plane = [['.' for i in range(n)] for j in range(n)]

        result = []
        self.dfs(plane, 0, n, result)

        return result


# test
solution = Solution()
print(solution.solveNQueens(4))
