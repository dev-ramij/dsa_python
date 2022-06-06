class Heapify:

    def heapify(self, arr, n, largest):
        i = largest
        left_idx = 2 * i
        right_idx = left_idx + 1
        if left_idx < n and arr[left_idx] > arr[largest]:
            largest = left_idx
        if right_idx < n and arr[right_idx] > arr[largest]:
            largest = right_idx
        # if largest is changed then we need to swap the parent
        # with it's largest child
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # maintain heapify after the largest has been changed
            self.heapify(arr, n, largest)

    # this function is used to build max heap
    # for that we need traverse from backward and build max heap for each node
    # we will leave the leaf node because it is already in max heap as it don't has any children
    # n//2+1 to n will be the leaf node
    def build_max_heap(self, arr, n):
        # insert 0 for simplicity
        arr.insert(0, 0)
        for i in range(n // 2, 0, -1):
            self.heapify(arr, n + 1, i)
        arr.pop(0)
        return arr


heap = Heapify()
print(heap.build_max_heap([10, 30, 50, 20, 35, 15], 6))
