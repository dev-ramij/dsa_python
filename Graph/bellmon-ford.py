

class Solution:
    # make distance all inifinite
    # init source as 0
    # iterate V-1 time
    # iterate for every edges
    # check if current distance is greater than the new distance or not
    def bellman_ford(self, V, edges, S):
        dist = [100000000] * V
        dist[S] = 0
        for ver in range(V):
            # edges = [source,destination,weight]
            # source --weight--> destination
            for edge in edges:
                source = edge[0]
                dest = edge[1]
                wt = edge[2]
                if dist[source] + wt < dist[dest]:
                    dist[dest] = dist[source]+wt
        return dist