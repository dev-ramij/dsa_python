from collections import deque


class Solution:

    def max_of_subarrays(self, arr, n, k):
        queue = deque()
        res = []
        # for the first window 
        for i in range(k):
            # if queue is not empty and the last element of the queue is lesser than current element
            # then we need to pop the last element
            while queue and arr[i] >= arr[queue[-1]]:
                queue.pop()
            # append the current element
            queue.append(i)
        # insert the first element's index to the result
        res.append(arr[queue[0]])
        # for the remaining list
        for i in range(k, n):
            # if first element's index is not in the sliding window
            # pop it
            while queue and queue[0] <= i - k:
                queue.popleft()
            # if queue is not empty and the last element of the queue is lesser than current element
            # then we need to pop the last element
            while queue and arr[i] >= arr[queue[-1]]:
                queue.pop()
            # append the current element's index
            queue.append(i)
            # insert the first element to the result
            res.append(arr[queue[0]])
        return res
        


ob = Solution()
ob.max_of_subarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], 9, 3)
