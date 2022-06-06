class Solution:

    def nextLargerElement(self, arr, n):
        if n == 0:
            return []
        if n == 1:
            return [-1]
        res_array = []
        stack = []
        arr.reverse()
        for i in range(n):
            if len(stack) == 0:
                res_array.append(-1)
                stack.append(arr[i])
                continue
            nextMax = -1
            while len(stack)>0:
                stackTop = stack[len(stack) - 1]
                if arr[i] < stackTop:
                    nextMax = stackTop
                    break
                else:
                    stack.pop()
            stack.append(arr[i])
            res_array.append(nextMax)
        res_array.reverse()
        return res_array

ob = Solution()
print(ob.nextLargerElement([1 ,3 ,2 ,4],4))