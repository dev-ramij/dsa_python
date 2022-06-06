# Given an integer x, find the square root of x.
# If x is not a perfect square, then return floor(√x).


class Solution:

    def floorSqrt(self, x):
            mid = x // 2
            last_rooted = 1
            if x == 1 or x == 0:
                return x
            first = 0
            last = x

            while first <= last:
                mid = (first + last) // 2
                sqr = mid * mid
                if sqr == x:
                    return mid
                if sqr > x:
                    last = mid - 1
                elif sqr < x:
                    first = mid + 1
                if sqr < x:
                    last_rooted = mid
            return last_rooted


ob = Solution()
print(ob.floorSqrt(5))