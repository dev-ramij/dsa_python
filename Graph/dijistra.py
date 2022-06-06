import heapq


class Solution:

    # First init distance infinity
    # then push the starting vertex to the min heap
    # pop the root from the heap until heap is empty
    # if visited continue
    # else check if weight is less than current distance then update it
    # marked it as visited
    # get all neighbors and check if it is visited and its current weight 
    # is less than the stored distance
    def dijkstra(self, V, adj, S):
        visited = [False] * V
        dist = [10000000] * V
        heap = []
        heapq.heappush(heap, (0, S))
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            wt = curr[0]
            vertex = curr[1]
            if visited[vertex]:
                continue
            if wt < dist[vertex]:
                dist[vertex] = wt
            neighbors = adj[vertex]
            visited[vertex] = True
            for neighbor in neighbors:
                neigh_vertex = neighbor[0]
                neigh_wt = neighbor[1]
                curr_wt = neigh_wt + wt
                if not visited[neigh_vertex] and curr_wt < dist[neigh_vertex]:
                    curr_wt = neigh_wt + wt
                    heapq.heappush(heap,(curr_wt,neigh_vertex))
        return dist