class Solution:

    def isSafe(self, board, row, col):

        for i in range(len(board)):
            rc = len(board[i])
            for j in range(rc):
                if (row == i or col == j):
                    if board[i][j] == 1:
                        return False
                elif abs(row - i) == abs(col - j) and board[i][j] == 1:
                    return False
        return True

    def solveQueen(self, board, result, row, n):
        if row == n:
            result.append(board)
            return True
        for j in range(n):
            if self.isSafe(board, row, j):
                board[row][j] = 1
                if (self.solveQueen(board, result, row + 1, n)):
                    return True
                board[row][j] = 0
        return False

    def nQueen(self, n):
        result = []
        board = []
        for i in range(n):
            board.append([])
            for j in range(n):
                board[i].append(0)

        for i in range(n):
            board[0][i] = 1
            self.solveQueen(board, result, 1, n)
            board = []
            for i in range(n):
                board.append([])
                for j in range(n):
                    board[i].append(0)
        res = []
        for r in range(len(result)):
            res.append([])
            for i in range(len(result[r])):
                for j in range(len(result[r][i])):
                    if result[r][i][j] == 1:
                        res[r].append(j + 1)
                        continue
        return res


objects = Solution()
print(objects.nQueen(4))