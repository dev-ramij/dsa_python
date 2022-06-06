class Solution:

    # First we will init visited all false
    # then do dfs from index 0
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        answer = []
        self.dfs(0, adj, visited, answer)
        return answer

    # First we will marked the vertices as True and 
    # append to our answer list
    # then we will do dfs for its neighbour which is not visited yet
    def dfs(self, vertice, adj, visited, ans):
        visited[vertice] = True
        neighbors = adj[vertice]
        ans.append(vertice)
        for neighbor in neighbors:
            if not visited[neighbor]:
                self.dfs(neighbor, adj, visited, ans)
