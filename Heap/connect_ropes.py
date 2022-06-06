from queue import PriorityQueue


class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr, n):
        pq = PriorityQueue()
        # push all the element
        for i in range(n):
            pq.put(arr[i])
        ropeSize = 0
        # get smallest first and second
        # do sum and put to the queue
        while pq.qsize() > 1:
            first = pq.get()
            second = pq.get()
            currSize = first + second
            ropeSize += currSize
            pq.put(currSize)
        return ropeSize

ob = Solution()
print(ob.minCost([4, 2, 7, 6, 9],5))
