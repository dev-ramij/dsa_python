# Given a non-negative number represented as a list of digits,
# add 1 to the number (increment the number represented by the digits).
# The digits are stored such that the most significant digit is first element of array.


class Solution:

    def increment(self, arr, N):
        extra = 1
        i = N-1
        has_first = False
        while extra != 0:
            if arr[i] == 9:
                arr[i] = 0
                extra = 1
                
                if i == 0:
                    has_first = True
                    break
                i -=1
            else:
                arr[i]+=1
                extra = 0
        print(arr)
        if has_first:
            return [1] + arr
        else:
            return arr


objects = Solution()
print(objects.increment([9], 1))
