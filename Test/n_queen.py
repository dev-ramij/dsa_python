class Solution:

    def isSafe(self, board, row, col, n):
        
        for j in range(n):
            if board[j][col] == 1:
                return False
            if row-j >= 0:
                if col-j >= 0 and board[row-j][col-j] == 1:
                    return False
                elif col + j < n - 1 and board[row-j][col + j] == 1:
                    return False
        return True

    def queenSolver(self, board, result, row, n):
        if row == n:
            result.append(board)
            return True
        for col in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = 1
                if self.queenSolver(board, result, row + 1, n):
                    return True
                board[row][col] = 0
        return False

    def n_queen(self, n):
        res = []
        board = []
        for i in range(n):
            board.append([])
            for j in range(n):
                board[i].append(0)

        self.queenSolver(board, res, 0, n)
        return res


ob = Solution()
print(ob.n_queen(5))
