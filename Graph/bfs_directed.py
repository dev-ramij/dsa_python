from queue import Queue

# We will use queue for BFS
# first item will be put into the queue
# then we will pop the item and add its connected nodes to the queue until queue is not empty
# besides that we will store which nodes are visited
# if once visited we don't need to do any bfs
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        queue = Queue()
        visited = []
        queue.put(0)
        while not queue.empty():
            currVer = queue.get()
            if currVer in visited:
                continue
            visited.append(currVer)
            nodes = adj[currVer]
            for ver in nodes:
                if ver not in visited:
                    queue.put(ver)
        return visited