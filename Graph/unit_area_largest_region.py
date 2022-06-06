class Solution:
    count = 0

    def findMaxArea(self, grid):
        adj = []
        # create adj matrix
        self.createAdjMat(grid,adj)
        n = len(adj)
        max_count = 0
        visited = [False] *n
        # perform dfs and increment count when new dfs is called
        for i in range(n):
            self.count = 0
            if not visited[i]:
                self.DFS(i,adj,visited)
                if max_count < self.count:
                    max_count = self.count
        return max_count

    def createAdjMat(self,grid,adj):
        n = len(grid)
        for i in range(n):
            col = len(grid[i])
            for j in range(col):
                idx = i*col + j
                adj.append(idx)
                adj[idx] = []
                if grid[i][j] == 1:
                    if i> 0 and grid[i-1][j] == 1:
                        adj[idx].append(((i-1)*col + j))
                    if i < n-1 and grid[i+1][j] == 1:
                        adj[idx].append(((i+1)*col + j))
                    if j > 0 and grid[i][j-1] == 1:
                        adj[idx].append((i*col + j-1))
                    if j < col-1 and grid[i][j+1] == 1:
                        adj[idx].append((i*col + j+1))
                    if i> 0 and j > 0 and grid[i-1][j-1] == 1:
                        adj[idx].append((i-1)*col + j-1)
                    if i >0 and j < col -1 and grid[i-1][j+1] == 1:
                        adj[idx].append((i-1)*col + j+1) 
                    if i < n-1 and j > 0 and grid[i+1][j-1] == 1:
                        adj[idx].append((i+1)*col + j-1)
                    if i < n-1 and j < col -1 and grid[i+1][j+1] == 1:
                        adj[idx].append((i+1)*col + j+1)

    def DFS(self, vertice, adj, visited):
        self.count+=1
        visited[vertice] = True
        neighbors = adj[vertice]
        for neighbor in neighbors:
            if not visited[neighbor]:
                self.DFS(neighbor,adj,visited)