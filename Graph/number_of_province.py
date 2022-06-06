from queue import Queue

class Solution:

    def BFS(self, adj, index, V, visited):
        queue = Queue()
        queue.put(index)
        while not queue.empty():
            currVer = queue.get()
            if visited[currVer]==1:
                continue
            nodes = adj[currVer]
            visited[currVer] = 1
            for i in range(V):
                if nodes[i] == 1 and visited[i] == 0:
                    queue.put(i)

    def numProvinces(self, adj, V):
        # first init visited all with zero as non-visited
        visited = [0] * V
        count = 0
        # get the first non visited vertices
        first_non_visited = visited.index(0)
        while first_non_visited > -1:
            # when we find one increment the count
            count += 1
            # do bfs of it
            self.BFS(adj, first_non_visited, V, visited)
            # if all vertices are visited then return count
            try:
                first_non_visited = visited.index(0)
            except:
                return count
        return count