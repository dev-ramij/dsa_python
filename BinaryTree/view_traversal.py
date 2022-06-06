# First store root node to the queue
# then remove the first element of the queue and print
# then put its left and right node
# then again repeat the step two
from queue import Queue
from tkinter.tix import Tree


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Traversal:

    def createBinaryTree(self):
        print("Enter data:")
        data = int(input())
        if data == -1:
            return None
        node = Node(data)
        print("Enter the left node data for", data)
        node.left = self.createBinaryTree()
        print("Enter the right node data for", data)
        node.right = self.createBinaryTree()
        return node

    def left_view_traverse(self, root):
        if root is None:
            return
        queue = Queue()
        # put the root first
        queue.put(root)
        res_arr = []
        res_arr.append(root.data)
        getLeftElement = False
        # delimeter or end of level 0
        queue.put("#")
        while not queue.empty():
            # pop the first item from the queue
            currNode = queue.get()
            if currNode == "#":
                # Left element will be the next node
                getLeftElement = True
                # put delimeter of the level
                # if queue is empty then no need to put #
                if not queue.empty():
                    queue.put("#")
            else:
                if getLeftElement == True:
                    res_arr.append(currNode.data)
                    getLeftElement = False
                if currNode.left is not None:
                    queue.put(currNode.left)
                if currNode.right is not None:
                    queue.put(currNode.right)

        print(res_arr)

    def right_view_traverse(self, root):
        if root is None:
            return
        queue = Queue()
        # put the root first
        queue.put(root)
        res_arr = []
        queue.put("#")
        # determind the last node
        lastNode = root
        while not queue.empty():
            # pop first item
            currNode = queue.get()
            if currNode == "#":
                # if we get delimeter then last node will be the right most node
                res_arr.append(lastNode.data)
                if not queue.empty():
                    queue.put("#")
            else:
                if currNode.left is not None:
                    queue.put(currNode.left)
                if currNode.right is not None:
                    queue.put(currNode.right)
                lastNode = currNode

        print(res_arr)

    def assign_horizontal_distance(self, node, value, hashMap):
        if node is None:
            return
        hashMap[node] = value
        # decrease value by 1 when it goes left
        self.assign_horizontal_distance(node.left, value - 1, hashMap)
        # increase value by 1 when it goes right
        self.assign_horizontal_distance(node.right, value + 1, hashMap)

    def top_view_traversal(self, root):
        # create a horizontal distance from the root
        # if goes left substract -1 and for right add 1
        horz_dis_map = {}
        self.assign_horizontal_distance(root, 0, horz_dis_map)
        queue = Queue()
        queue.put(root)
        queueMap = {}
        while not queue.empty():
            currNode = queue.get()
            # get the value of horizantol distance
            horz_dis = horz_dis_map[currNode]
            # if it is not present in queuemap put it
            # We are checking not present because if we update with lower level value
            # then we can't get the top view
            if horz_dis not in queueMap:
                queueMap[horz_dis] = currNode.data
            if currNode.left:
                queue.put(currNode.left)
            if currNode.right:
                queue.put(currNode.right)
        # used to store queue map keys
        queueMapKeys = []
        for key in queueMap.keys():
            queueMapKeys.append(key)
        res_arr = []
        # sort for viewing as ascending order
        queueMapKeys.sort()
        # append the sorted value
        for key in queueMapKeys:
            res_arr.append(queueMap[key])

        return res_arr

    def bottom_view_traversal(self, root):
        # create a horizontal distance from the root
        # if goes left substract -1 and for right add 1
        horz_dis_map = {}
        self.assign_horizontal_distance(root, 0, horz_dis_map)
        queue = Queue()
        queue.put(root)
        queueMap = {}
        while not queue.empty():
            currNode = queue.get()
            # get the value of horizantol distance
            horz_dis = horz_dis_map[currNode]
            # update the queueMap value to its lowest level value
            queueMap[horz_dis] = currNode.data
            if currNode.left:
                queue.put(currNode.left)
            if currNode.right:
                queue.put(currNode.right)
        # used to store queue map keys
        queueMapKeys = []
        for key in queueMap.keys():
            queueMapKeys.append(key)
        res_arr = []
        # sort for viewing as ascending order
        queueMapKeys.sort()
        # append the sorted value
        for key in queueMapKeys:
            res_arr.append(queueMap[key])

        return res_arr


tree = Traversal()
root = tree.createBinaryTree()
tree.bottom_view_traversal(root)
# tree.left_view_traverse(root)
# tree.right_view_traverse(root)