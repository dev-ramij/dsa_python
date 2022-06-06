class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):

        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


ob = Solution()
print(ob.bubbleSort([4, 1, 3, 9, 7], 5))
