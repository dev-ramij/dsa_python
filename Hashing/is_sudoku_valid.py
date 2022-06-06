class Solution:

    def isValid(self, mat):

        hashMap = {}
        # check for row
        for row in range(9):
            hashMap = {}
            for col in range(9):
                value = mat[row][col]
                if value != 0:
                    if value in hashMap:
                        return 0
                    else:
                        hashMap[value] = row

        # check for column
        # traverse through column
        for col in range(9):
            hashMap = {}
            for row in range(9):
                value = mat[row][col]
                if value != 0:
                    if value in hashMap:
                        return 0
                    else:
                        hashMap[value] = col

        # check for block
        # we need to traverse the row and column block
        # we have 3 row block and 3 col block
        for rowBlock in range(3):
            for colBlock in range(3):
                hashMap = {}
                rowindex = rowBlock * 3
                colIndex = colBlock * 3
                # traverse from rowIndex to rowIndex+3
                for row in range(rowindex, rowindex + 3):
                    # traverse from colIndex to colIndex+3
                    for col in range(colIndex, colIndex + 3):
                        value = mat[row][col]
                        if value != 0:
                            if value in hashMap:
                                return 0
                            else:
                                hashMap[value] = row

        return 1


ob = Solution()
print(
    ob.isValid([[0, 0, 0, 3, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 2, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]))
