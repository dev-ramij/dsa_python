import re


class Solution:

    def isSafe(self, board, row, col, num):
        cellRow = row - row % 3
        cellCol = col - col % 3
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i == row or j == col) and board[i][j] == num:
                    return False
                if (i >= cellRow and i <
                    (cellRow + 3)) and (j >= cellCol and j < cellCol + 3
                                        ) and board[i][j] == num:

                    return False

        return True

    def findNonZero(self, board, index):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    index[0] = i
                    index[1] = j
                    return True

        return False

    def solveSudokuHelper(self, board):
        l = [0, 0]

        if (not self.findNonZero(board, l)):
            return True

        row = l[0]
        col = l[1]
        for k in range(1, 10):
            if self.isSafe(board, row, col, k):
                board[row][col] = k
                if self.solveSudokuHelper(board):
                    return True
                board[row][col] = 0

        return False

    def SolveSudoku(self, grid):
        self.solveSudokuHelper(grid)
        return True

    #Function to print grids of the Sudoku.
    def printGrid(self, arr):
        stri = ""
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                stri += str(arr[i][j]) + " "
            print(stri)
            stri = ""


ob = Solution()
print(
    ob.SolveSudoku([[3, 0, 6, 5, 0, 8, 4, 0, 0], [5, 2, 0, 0, 0, 0, 0, 0, 0],
                    [0, 8, 7, 0, 0, 0, 0, 3, 1], [0, 0, 3, 0, 1, 0, 0, 8, 0],
                    [9, 0, 0, 8, 6, 3, 0, 0, 5], [0, 5, 0, 0, 9, 0, 6, 0, 0],
                    [1, 3, 0, 0, 0, 0, 2, 5, 0], [0, 0, 0, 0, 0, 0, 0, 7, 4],
                    [0, 0, 5, 2, 0, 6, 3, 0, 0]]))
