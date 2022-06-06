from tkinter.messagebox import NO
from turtle import right
from wsgiref import headers


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # creating a node
        node = Node(data, self.head)
        # assign the node to head
        self.head = node

    def insert_at_end(self, data):
        # creating a node
        node = Node(data, None)
        # if the list is empty
        if self.head is None:
            self.head = node
            return
        itr = self.head
        # iterate the linked list
        while itr:
            # find the last node
            if itr.next is None:
                itr.next = node
                return
            # goto the next node
            itr = itr.next

    def delete_at_begining(self):
        if self.head is None:
            print("List is already empty")
            return
        next_node = self.head.next
        self.head = next_node

    def delete_at_end(self):
        if self.head is None:
            print("List is already empty")
            return
        itr = self.head
        prev_node = None
        # iterate the linked list
        while itr:
            # find the last node
            if itr.next is None:
                if prev_node is None:
                    self.head = None
                    return
                prev_node.next = None
                itr = None
                break
            # goto the next node
            prev_node = itr
            itr = itr.next

    def insert_at_position(self, data, pos):
        index = 0
        itr = self.head
        # if list is empty
        if self.head is None:
            if pos == 0:
                node = Node(data, None)
                self.head = node
                return
            else:
                print("Can't put at the position ", pos)
                return

        prev_node = None
        # iterate the list
        while itr:
            # when we get the position
            if index == pos:
                node = Node(data, itr)
                # If not the first node
                if prev_node is not None:
                    prev_node.next = node
                # for first node
                else:
                    self.head = node
                return
            prev_node = itr
            itr = itr.next
            index += 1
        if index == pos:
            self.insert_at_end(data)
            return
        print("Can't put at the position ", pos)

    def delete_at_position(self, pos):
        index = 0
        itr = self.head
        if self.head is None:
            print("List is already empty")

        prev_node = None

        while itr:
            if index == pos:
                if prev_node is not None:
                    prev_node.next = itr.next
                else:
                    self.head = itr.next
                return
            prev_node = itr
            itr = itr.next
            index += 1
        if index == pos:
            self.delete_at_end()
            return
        print("Can't delete at the position", pos)

    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
            return
        # pointing to the head
        itr = self.head
        # iterate while not getting none
        itstr = ""
        while itr:
            itstr += str(itr.data) + " --> "
            # go to the next node
            itr = itr.next
        print(itstr + "null")

    def rotateByK(self, head, k):

        # code here
        if head is None:
            return
        # rotate head needs to return
        rotate_head = None
        itr = head
        left_head = itr
        i = 0
        # cut the left linked list for appending at last 
        while i < k-1:
            itr = itr.next
            i+=1
        rotate_head = itr.next
        # if k is the length of linked list then we don't need to do anything 
        # return the left head 
        if rotate_head is None:
            return left_head
        itr.next = None
        rotate_itr = rotate_head
        # find the last item of the list 
        while rotate_itr.next:
            rotate_itr = rotate_itr.next
        # append the left linked list
        rotate_itr.next = left_head
        return rotate_head


def printLinkedList(head):
    if head is None:
        print("Linked list is empty")
        return
    # pointing to the head
    itr = head
    # iterate while not getting none
    itstr = ""
    while itr:
        itstr += str(itr.data) + " --> "
        # go to the next node
        itr = itr.next
    print(itstr + "null")


ll = LinkedList()
for i in range(1, 9):
    ll.insert_at_end(i)

printLinkedList(ll.rotateByK(ll.head, 4))
# ll.delete_at_end()
# ll.printLinkedList()