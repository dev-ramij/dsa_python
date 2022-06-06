# First store root node to the queue
# then remove the first element of the queue and print
# then put its left and right node
# then again repeat the step two
from queue import Queue


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

    def level_order_traverse(self, root):
        if root is None:
            return
        queue = Queue()
        # put the root first
        queue.put(root)
        queue.put("#")
        res_arr = []
        while not queue.empty():
            currNode = queue.get()
            if currNode == "#":
                stri = ""
                for i in range(len(res_arr)):
                    stri+= str(res_arr[i]) + " "
                res_arr = []
                print(stri)
                if not queue.empty():
                    queue.put("#")
            else:
                res_arr.append(currNode.data)
                if currNode.left is not None:
                    queue.put(currNode.left)
                if currNode.right is not None:
                    queue.put(currNode.right)


tree = Traversal()
root = tree.createBinaryTree()
tree.level_order_traverse(root)