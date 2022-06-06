class Solution:

    def select(self, arr, i):
        # get the smallest index
        index = i
        for idx in range(i, len(arr)):
            if arr[idx] < arr[index]:
                index = idx
        return index

    def selectionSort(self, arr, n):
        for i in range(n):
            # select smallest index from the unsorted array
            smallest_idx = self.select(arr, i)
            # check if i is not the smallest index to avoid unneccessary swap
            if i != smallest_idx:
                # swap with smallest index
                arr[i], arr[smallest_idx] = arr[smallest_idx], arr[i]


ob = Solution()
ob.selectionSort([4, 1, 3, 9, 7], 5)
