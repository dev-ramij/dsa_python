import sys
class Solution:
    index = 0

    def canRepresentBSTUtil(self, arr, minValue, maxValue, n):
        if self.index >= n:
            return
        # store the rootData
        rootData = arr[self.index]

        if rootData >= minValue and rootData <= maxValue:
            self.index += 1
            # for left sub tree
            # if it is not a left sub tree then index will not be updated
            # and it goes to the right sub tree
            self.canRepresentBSTUtil(arr, minValue, rootData,n)
            # for right sub tree
            self.canRepresentBSTUtil(arr,rootData,maxValue,n)

        
    def canRepresentBST(self, arr, N):
        # when it traverse the whole array without violating the condition then it is valid
        self.canRepresentBSTUtil(arr, - sys.maxsize, sys.maxsize, N)
        if self.index == N:
            return 1
        return 0
