class Solution:

    def insert(self, alist, index, n):
        #code here
        pass

    #Function to sort the list using insertion sort algorithm.
    def insertionSort(self, alist, n):
        temp = -1
        # iterate through the list
        for i in range(1, n):
            # store current value from the unsorted part
            temp = alist[i]
            # iterate the sorted part and try to get where temp will be placed
            for j in range(i - 1, -1, -1):
                # if greater then shift this value to its right
                # and make it current value none
                if temp < alist[j]:
                    alist[j + 1] = alist[j]
                    alist[j] = None
                else:
                    alist[j+1] = temp
                    break
            # we can't check the first value so here we check it
            if alist[0] is None:
                alist[0] = temp
                
        print(alist)


ob = Solution()
ob.insertionSort([24, 18 ,38 ,43, 14, 40, 1, 54], 8)
