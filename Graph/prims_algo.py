import heapq

class Solution:

    # we are using prims alog here
    # We will create a min heap 
    # We will push (weight,vertice) because first item from the tuple is used to compare
    # First, we will push (0,0) in min heap
    # then pop the min item from the heap until heap is not empty
    # check if node is visited then no need any operation
    # if not add the sum and marked as visited
    # Get all the neightbors
    # Then if neighbor is not visited push it
    def spanningTree(self, V, adj):
        heap = []
        visited = [False] * V
        sum_weights = 0
        # (weight, vertice)
        heapq.heappush(heap, (0, 0))
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            weight = curr[0]
            ver = curr[1]
            if visited[ver]:
                continue
            sum_weights += weight
            neighbors = adj[ver]
            visited[ver] = True
            for neighbor in neighbors:
                ver = neighbor[0]
                weight = neighbor[1]
                if not visited[ver]:
                    heapq.heappush(heap, (weight, ver))
        return sum_weights



ob = Solution()
ob.spanningTree(1, 2)
