class Solution:
    
    # we will do DFS first
    # we will store the answer in reverse order
    # for example 1->0<-2, answer may be 2 1 0
    # so when we do dfs first we will get the 0 value which has less responsibility
    # so we will put it first then 1 and then 2
    def topoSort(self, V, adj):
        visited = [False] * V
        ans =[]
        for i in range(V):
            if not visited[i]:
                self.DFS(i,adj,visited,ans)
        return ans

    def DFS(self,ver,adj,visited,ans):
        visited[ver] = True
        neighbors = adj[ver]
        for neighbor in neighbors:
            if not visited[neighbor]:
                self.DFS(neighbor,adj,visited,ans)
        ans.append(ver)
        
