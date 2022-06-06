# For an integer N find the number of trailing zeroes in N!.


class Solution:

    def trailingZeroes(self, N):
        i = 1
        value = N
        res = 0
        while True:
            value = N // (5 ** i)
            res +=value
            i+=1
            if value < 5:
                break
        return res

onj = Solution()
print(onj.trailingZeroes(25))
