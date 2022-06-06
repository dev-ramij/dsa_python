from queue import PriorityQueue


class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, k):
        pq = PriorityQueue()
        pq.queue
        res_arr = []
        # put all element in min heap manner
        for i in range(len(arr)):
            for j in range(k):
                pq.put(arr[i][j])
        # pop the lowest element
        while not pq.empty():
            res_arr.append(pq.get_nowait())
        return res_arr

ob = Solution()
print(ob.mergeKArrays([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))
