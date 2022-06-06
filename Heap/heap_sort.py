
class Heap:

    # delete the root node and return the element
    def delete(self, arr, n):
        i = 1
        arr[i], arr[n] = arr[n], arr[i]
        while i < n:
            largest = i
            left = 2 * i
            right = left + 1
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                i = largest
            else:
                break

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

    # First it will build the max heap
    # then delete its root and insert to res_arr
    # after all delete just reverse the array for ascending order
    def heap_sort(self, arr, n):
        # insert 0 for simplicity
        arr.insert(0, 0)
        for i in range(n // 2, 0, -1):
            self.heapify(arr, n + 1, i)
        for i in range(1, n+1):
            self.delete(arr, n+1-i)
        arr.pop(0)
        return arr


heap = Heap()
print(heap.heap_sort([10, 30, 50, 20, 35, 15], 6))
