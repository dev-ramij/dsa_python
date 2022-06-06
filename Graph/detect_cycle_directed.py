
# This is same as detected cycle in udirected but there is a little difference
# we need a recursion stack here
# Recurion stack is used for every recursion
# For example 0-> 1 <- 2 here see no cycle present
# but 1 is visited in when it starts from 0 then dfs is terminated 
# and then 2 is not visited so we need check for 2 but in that case 1 is again visited
# and it seems to be a cycle
# so we are using recursion stack when we enter into any dfs recursion we make it true
# and when exiting we will do it as false
# if visited and recursion_stack has the vertices then we can say it forms a cycle
class Solution:

    def isCyclic(self, V, adj):
        visited = [False] * V
        recursion_stack = [False] * V
        for i in range(V):
            if not visited[i]:
                if self.dfs(i, adj, visited, recursion_stack):
                    return True
        return False

    def dfs(self, vertice, adj, visited, recursion_stack):
        visited[vertice] = True
        # set the vertices
        recursion_stack[vertice] = True
        neighbors = adj[vertice]
        for neighbor in neighbors:
            # if not visited then we do dfs for its neighbors
            if not visited[neighbor]:
                if self.dfs(neighbor, adj, visited, recursion_stack):
                    return True
            # if visited and recursion stack is true
            elif recursion_stack[neighbor]:
                return True
        # reset the vertices
        recursion_stack[vertice] = False
        return False