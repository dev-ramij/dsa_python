from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    prev = None
    head = None

    # First convert root's left then root then right sub tree into dll
    # if prev is null that means first node for dll we are setting it as head
    # else the left of root will be prev and right of the prev will be root
    # return head
    def bToDLL(self, root):
        if root is None:
            return None
        self.bToDLL(root.left)
        if self.prev is None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root

        self.prev = root

        self.bToDLL(root.right)
        return self.head
