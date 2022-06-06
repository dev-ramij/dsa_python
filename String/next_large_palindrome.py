
# Algorithm:
# 1. Split from the mid point
# 2. For the left array find the next higher number
# 3. First, start from the second last
# 4. compare it with its right element
# 5. If right element is greater than it then that will be the swap_pointer
# 6. Get the right array by spliting from swap_pointer
# 7. Find the next higher value of the swap_pointer value from the right array
# 8. Swap this value with swap_pointer value
# 9. Now get the left array and right array divide by the swap_pointer. 0-swap_pointer, swap_pointer+1,n
# 10. Sort the right array then merge and return
# 11. Result will be left_arr + midValue(for odd number) + right_arr (reverse of left array)

class Solution:

    def getNextHigher(self, arr, value):
        n = len(arr)
        smallest_idx = 0
        for i in range(1, n):
            if arr[i] > value and arr[i] < arr[smallest_idx]:
                smallest_idx = i
        return smallest_idx

    def getNextGretearValue(self, num_arr):
        n = len(num_arr)
        if n == 2:
            if num_arr[0] < num_arr[1]:
                num_arr[0], num_arr[1] = num_arr[1], num_arr[0]
                return num_arr
            else:
                return -1
        
        swap_pointer = n - 2

        while swap_pointer >= 0:
            # find where arr[i] < arr[i+1] 
            if num_arr[swap_pointer] < num_arr[swap_pointer + 1]:
                # get the right array
                right_arr = num_arr[swap_pointer + 1:]
                # get  the next higher value index of the swap_pointer
                swap_val_idx = swap_pointer + self.getNextHigher(
                    right_arr, num_arr[swap_pointer]) + 1
                num_arr[swap_pointer], num_arr[swap_val_idx] = num_arr[
                    swap_val_idx], num_arr[swap_pointer]
                right_arr = num_arr[swap_pointer + 1:]
                right_arr.sort()
                left_arr = num_arr[:swap_pointer + 1]
                return left_arr + right_arr
            swap_pointer -= 1
        return -1

    def nextPalin(self, N):
        n = len(N)
        mid = n // 2
        midValue = -1
        # for odd digit there is midvalue
        if n % 2 == 1:
            midValue = int(N[mid])
        left_str = []
        for i in range(mid):
            left_str.append(int(N[i]))
        if len(left_str) == 1:
            return -1
        # Get the next greater value of the left array
        next_res = self.getNextGretearValue(left_str)
        if next_res == -1:
            return -1
        else:
            res_str = ""
            # join left array result
            res_str += "".join(map(str, next_res))
            # join midvalue if any
            if midValue > -1:
                res_str += str(midValue)
            # reverse the left array and join
            next_res.reverse()
            res_str += "".join(map(str, next_res))
            return res_str


ob = Solution()
print(ob.nextPalin("454121454"))
