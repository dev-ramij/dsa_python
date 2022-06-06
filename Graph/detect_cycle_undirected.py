class Solution:
    # We will perform for all non-visited vertices because graph may be disconnected
    # if dfs is True then there is a cycle
    def isCycle(self, V, adj):
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if self.dfs(i, adj, visited, -1):
                    return True
        return False

    # First mark it as visited
    # check dfs for all neighbor
    # Two condition arised:
    # 1. visited: Then check if the neighbour is parent or not if parent 
    #             then it is not a cycle it is happening because of unidirected
    # 2. not visited: Now check for all neighbors of it if they have cycle or not
    def dfs(self, vertice, adj, visited, parent):
        visited[vertice] = True
        neighbors = adj[vertice]
        for neighbor in neighbors:
            # condition 2
            if not visited[neighbor]:
                if self.dfs(neighbor,adj,visited,vertice):
                    return True
            # condition 1
            elif parent != neighbor:
                return True
        return False
