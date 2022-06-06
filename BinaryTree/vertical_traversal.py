from queue import Queue

# We need to calculate horizonatal distance for each node
# But we need to do it level wise means level n element should be print before level >n
# We are using hashmap which store hd as key and data of the hd as array
# Then we can print acsending order

class Solution:
    
    def levelOrder(self, root, hashMap):
        queue = Queue()
        # we are putting object of node and level
        queue.put({"node": root, "level": 0})
        while not queue.empty():
            currItem = queue.get()
            if currItem["level"] not in hashMap:
                hashMap[currItem["level"]] = [currItem["node"].data]
            else:
                hashMap[currItem["level"]].append(currItem["node"].data)
            if currItem["node"].left:
                queue.put({"node": currItem["node"].left, "level": currItem["level"] - 1})
            if currItem["node"].right:
                queue.put({"node": currItem["node"].right, "level": currItem["level"] + 1})

    def verticalOrder(self, root):
        hashMap = {}

        self.levelOrder(root, hashMap)
        res_arr = []
        for value in sorted(hashMap):
            res_arr += hashMap[value]
        return res_arr