class Heap:

    def __init__(self, arr) -> None:
        self.arr = []
        self.arr.append(0)
        for i in range(1, len(arr) + 1):
            self.arr.append(arr[i - 1])

    def getParentNode(self, index):
        parentIdx = index // 2
        return parentIdx

    def getLeftNode(self, index):
        leftIdx = 2 * index
        return leftIdx

    def getRightNode(self, index):
        rightIdx = 2 * index + 1
        return rightIdx

    # first insert at last
    # then check if parent is lesser or not
    # if lesser then swap otherwise break
    def insert(self, value):
        # insert at last
        self.arr.append(value)
        n = len(self.arr)
        i = n - 1
        # stop when we are in root position
        while i > 1:
            parentNode = self.getParentNode(i)
            if self.arr[parentNode] < self.arr[i]:
                self.arr[parentNode], self.arr[i] = self.arr[i], self.arr[
                    parentNode]
                i = parentNode
            else:
                break

    # first swap first node to last node
    # then delete the last node
    # now heapify from first index
    # then compare the leftnode and rightnode which is greater
    # greater node will be placed at the deleted node
    # pop the last element
    def delete(self):
        i = 1
        n = len(self.arr)
        self.arr[i], self.arr[n - 1] = self.arr[n - 1], self.arr[i]
        self.arr.pop()
        n = n - 1
        while i < n:
            leftNode = self.getLeftNode(i)
            rightNode = self.getRightNode(i)
            if leftNode < n - 1 and rightNode < n - 1:
                if self.arr[leftNode] > self.arr[rightNode]:
                    self.arr[leftNode], self.arr[i] = self.arr[i], self.arr[
                        leftNode]
                    i = leftNode
                else:
                    self.arr[rightNode], self.arr[i] = self.arr[i], self.arr[
                        rightNode]
                    i = rightNode
            elif leftNode > n - 1 and rightNode > n - 1:
                break
            else:
                self.arr[leftNode], self.arr[i] = self.arr[i], self.arr[
                    leftNode]
                i = leftNode


heap = Heap([50, 40, 45, 30, 20, 35, 10])
heap.insert(60)
print(heap.arr)
heap.insert(45)
print(heap.arr)
heap.delete()
print(heap.arr)
