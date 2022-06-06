# Given a positive integer N, return the Nth row of pascal's triangle.
# Pascal's triangle is a triangular array of the binomial coefficients
# formed by summing up the elements of previous row.


class Solution:

    def nthRowOfPascalTriangle(self, n):
        mod = 1000000007
        matrix = []
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append((matrix[i - 1][j - 1] + matrix[i - 1][j])%mod)
            matrix.append(row)

        return matrix[n - 1]


ob = Solution()
print(ob.nthRowOfPascalTriangle(74))
