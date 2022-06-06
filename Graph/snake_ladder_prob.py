from queue import Queue

class Solution:
    
    def generateArr(self, block, n, arr):
        # init with its index
        for i in range(31):
            block.append(i)
        i = 0
        # put all snake and ladder
        while i < len(arr):
            block[arr[i]] = arr[i + 1]
            i+=2
        
            
    def minThrow(self, N, arr):
        block = []
        self.generateArr(block, N, arr)
        queue = Queue()
        queue.put(1)
        step = 0
        visited = [False]*31
        while not queue.empty():
            curr = queue.get()
            # if we get end point increment the step and put #
            if curr == "#":
                step+=1
                queue.put("#")
                continue
            if curr == 30:
                return step
            if curr == 1:
                queue.put("#")
            # BFS
            for i in range(1, 7):
                if curr+i>30:
                    continue
                idx = block[curr + i]
               
                if not visited[idx]:
                    visited[idx] = True
                    queue.put(idx)    
        return step