from queue import PriorityQueue


class Solution:

    def kthLargest(self, k, arr, n):
        pq = PriorityQueue(k)
        res_arr = []
        # iterate the array
        for i in range(n):
            # if pq is less than k then put the array
            if pq.qsize() <k:
                pq.put(arr[i])
            # if top of the queue (minimum element) is less than the value
            # then remove the top and insert the new one
            elif arr[i] > pq.queue[0]:
                pq.get()
                pq.put(arr[i])

            if pq.qsize()<k:
                res_arr.append(-1)
            else:
                res_arr.append(pq.queue[0])
        return res_arr


ob = Solution()
print(ob.kthLargest(4, [1, 2, 3, 4,2, 4, 6], 7))
