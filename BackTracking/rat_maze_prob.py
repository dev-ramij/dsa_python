class Solution:

    def getPath(self, result, track, paths, currPoint, board, n):
        row = currPoint[0]
        col = currPoint[1]
        print(currPoint, paths)
        hasPath = False
        if row == n - 1 and col == n - 1:
            result.append(track)
            return
            
        if row < n - 1 and board[row + 1][col] == 1:
            hasPath = True
            cp = [row + 1, col]
            if cp in paths:
                paths = []
                return
            else:
                paths.append(cp)
                self.getPath(result, track + "D", paths, cp, board, n)
        if col < n - 1 and board[row][col + 1] == 1:
            hasPath = True
            cp = [row, col + 1]
            if cp in paths:
                paths = []
                return
            else:
                paths.append(cp)
                self.getPath(result, track + "R", paths, cp, board, n)
        if row > 0 and board[row - 1][col] == 1:
            hasPath = True
            cp = [row - 1, col]
            if cp in paths:
                paths = []
                return
            else:
                paths.append(cp)
                self.getPath(result, track + "U", paths, cp, board, n)
        if col > 0 and board[row][col - 1] == 1:
            hasPath = True
            cp = [row, col - 1]
            if cp in paths:
                paths = []
                return
            else:
                paths.append(cp)
                self.getPath(result, track + "L", paths, cp, board, n)
        if not hasPath:
            return

    def findPath(self, m, n):
        result = []
        paths = []
        self.getPath(result, "", paths, [0, 0], m, n)
        result.sort()
        return result


ob = Solution()
print(ob.findPath([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]], 4))
