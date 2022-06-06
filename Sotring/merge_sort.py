from turtle import left, right


class Solution:

    def merge(self, arr, l, m, r):
        
        temp = arr.copy()
        left_pointer = l
        right_pointer = m + 1
        k = l
        # check two arrays and which is smaller assigned to temp array
        while left_pointer <= m and right_pointer <= r:
            if arr[left_pointer] < arr[right_pointer]:
                temp[k] = arr[left_pointer]
                left_pointer += 1
            else:
                temp[k] = arr[right_pointer]
                right_pointer += 1
            k += 1
        # if any right array element is left then put it into temp array
        if left_pointer > m:
            while right_pointer <= r:
                temp[k] = arr[right_pointer]
                right_pointer += 1
                k += 1
        else:
            while left_pointer <= m:
                temp[k] = arr[left_pointer]
                left_pointer += 1
                k += 1
        # copy the temp array to original one
        # in temp array from l to k is changed so we will update the part only
        for i in range(l, k):
            arr[i] = temp[i]

    def mergeSort(self, arr, l, r):
        #code here
        if l < r:
            mid = (l + r) // 2
            # divide the array into two part separate by mid
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            # merge two sorted array 
            self.merge(arr, l, mid, r)

ob = Solution()
ob.mergeSort([4, 1, 3, 9, 7], 0, 4)
