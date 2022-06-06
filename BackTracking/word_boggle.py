class Solution:

    def solveWord(self, dics, board, searchBoard, tracks, results, idx, str,
                  rowLast, colLast):
        if str == dics:
            if str not in results:
                results.append(str)
            return
        searchEl = dics[idx]
        for item in searchBoard:
            i = item[0]
            j = item[1]
            if board[i][j] == searchEl:
                tracks.append([i, j])
                newBoard = []
                rowList = [i]
                colList = [j]
                if i > 0:
                    rowList.append(i - 1)
                if i < rowLast:
                    rowList.append(i + 1)
                if j > 0:
                    colList.append(j - 1)
                if j < colLast:
                    colList.append(j + 1)
                for row in rowList:
                    for col in colList:
                        if [row, col] not in tracks:
                            newBoard.append([row, col])
                self.solveWord(dics, board, newBoard, tracks, results, idx + 1,
                               str + searchEl, rowLast, colLast)

    def wordBoggle(self, board, dictionary):

        results = []
        str = ""
        rowLast = len(board) - 1
        colLast = len(board[0]) - 1
        newBoard = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                newBoard.append([i, j])
        for value in dictionary:
            self.solveWord(value, board, newBoard, [], results, 0, str,
                           rowLast, colLast)
        return results


ob = Solution()
print(
    ob.wordBoggle([["d", "d"], ["b", "f"], ["e", "c"], ["b", "c"], ["d", "c"]],
                  ["bcd", "db"]))
