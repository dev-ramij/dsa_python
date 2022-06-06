class Solution:

    def quickSort(self, arr, low, high):
        # if low is greater than high then we don't need to sort
        if low < high:
            # get the pivot element by partioning
            pivot = self.partition(arr, low, high)
            # quick sort left part of the pivot
            self.quickSort(arr, low, pivot - 1)
            # quick sort of the right part of the pivot
            self.quickSort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        # take low element as pivot
        pivot = arr[low]
        i = low
        j = high
        # iterate until i is less than j
        while i < j:
            # increment i until we get the greater element of the pivot
            while i < len(arr) and arr[i] <= pivot:
                i += 1
            # increment j until we get the lesser element of the pivot
            while j > 0 and arr[j] > pivot:
                j -= 1
            # swap so that small element comes first and greater element goes last
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        # swap the j to low so that pivot element will be at middle of the lesser and greater part
        arr[j], arr[low] = arr[low], arr[j]
        return j


ob = Solution()
ob.quickSort([4, 1, 3, 9, 7], 0, 4)
