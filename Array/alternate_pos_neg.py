# Given an unsorted array Arr of N positive and negative numbers.
# Your task is to create an array of alternate positive and
# negative numbers without changing the relative order of positive and negative numbers.
# Note: Array should start with positive number.


class Solution:

    def rearrange(self, arr, n):
        pos_stack = []
        neg_stack = []
        for i in range(n):
            if arr[i] < 0:
                neg_stack.append(arr[i])
            else:
                pos_stack.append(arr[i])

        pos = True
        if len(pos_stack) == 0:
            pos = False
        res = []
        pos_idx = 0
        neg_idx = 0
        for i in range(n):
            if pos:
                res.append(pos_stack[pos_idx])
                pos_idx += 1
                if neg_idx < len(neg_stack):
                    pos = False
            else:
                res.append(neg_stack[neg_idx])
                neg_idx += 1
                if pos_idx < len(pos_stack):
                    pos = True
        return res


ob = Solution()
print(ob.rearrange([9, 4, -2 ,-1, 5, 0 ,-5 ,-3, 2], 9))
