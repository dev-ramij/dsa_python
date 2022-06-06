
# use bellmon-ford to fill shortest distance
# iterate one more time if distance is updated
# then cycle is present
class Solution:
    def isNegativeWeightCycle(self, n, edges):
        dist = [100000000] * n
        dist[0] = 0
        for ver in range(n):
            for edge in edges:
                source = edge[0]
                dest = edge[1]
                wt = edge[2]
                if dist[source] + wt < dist[dest]:
                    dist[dest] = dist[source]+wt
        negative_cycle = 0
        for edge in edges:
            source = edge[0]
            dest = edge[1]
            wt = edge[2]
            if dist[source] + wt < dist[dest]:
                negative_cycle = 1
                dist[dest] = dist[source]+wt

        return negative_cycle