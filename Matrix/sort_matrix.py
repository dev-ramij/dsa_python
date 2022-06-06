# Given an NxM 2D matrix, rearrange such that
# Each diagonal in the lower left triangle of the rectangular grid is sorted in ascending order.
# Each diagonal in the upper right triangle of the rectangular grid is sorted in descending order.
# The major diagonal in the grid starting from the top-left corner is not rearranged.


class Solution:

    def diagonalSort(self, matrix, n, m):
        for i in range(n):
            print("III")
            for j in range(m):
                diagonal = []
                print(i,j)
                if i == j:
                    continue
                if j > i:
                    r, c = i, j
                    for i in range(m - j):
                        if r == n  or c == m :
                            break
                        diagonal.append(matrix[r][c])
                        r += 1
                        c += 1
                    print(diagonal)


objects = Solution()
print(
    objects.diagonalSort(
        [[3, 6, 3, 8, 2], [4, 1, 9, 5, 9], [5, 7, 2, 4, 8], [8, 3, 1, 7, 6]],
        4, 5))
