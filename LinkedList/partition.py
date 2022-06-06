
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


def partition(head, x):
    lesser_head = None
    lesser_itr = None
    equal_head = None
    equal_itr = None
    greater_head = None
    greater_itr = None
    itr = head
    while itr:
        node = Node(itr.data, None)
        if itr.data < x:
            if lesser_itr is None:
                lesser_head = node
                lesser_itr = node
            else:
                lesser_itr.next = node
                lesser_itr = lesser_itr.next
        elif itr.data == x:
            if equal_itr is None:
                equal_head = node
                equal_itr = node
            else:
                equal_itr.next = node
                equal_itr = equal_itr.next
        else:
            if greater_itr is None:
                greater_head = node
                greater_itr = node
            else:
                greater_itr.next = node
                greater_itr = greater_itr.next
        itr = itr.next
    if lesser_head and greater_head and equal_head:
        equal_itr.next = greater_head
        lesser_itr.next = equal_head
        return lesser_head
    elif lesser_head and equal_head:
        lesser_itr.next = equal_head
        return lesser_head
    elif lesser_head and greater_head:
        lesser_itr.next = greater_head
        return lesser_head
    elif equal_head and greater_head:
        equal_itr.next = greater_head
        return equal_head
    elif lesser_head:
        return lesser_head
    elif equal_head:
        return equal_head
    elif greater_head:
        return greater_head


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
ll.insert_at_end(1)
ll.insert_at_end(4)
ll.insert_at_end(2)
ll.insert_at_end(10)
# ll.insert_at_end(2)
# ll.insert_at_end(3)


printLinkedList(partition(ll.head, 3))
# ll.delete_at_end()
# ll.printLinkedList()