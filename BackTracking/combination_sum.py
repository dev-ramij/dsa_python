class Solution:

    def combineHelp(self, arr, temp_arr, results, remaining, idx):
        if remaining == 0:
            if temp_arr not in results:
                results.append(list(temp_arr))
            return
        if remaining < 0:
            return
        for i in range(idx, len(arr)):
            if remaining - arr[i] >= 0:
                temp_arr.append(arr[i])
                self.combineHelp(arr, temp_arr, results, remaining - arr[i], i)
                temp_arr.pop()

    def combinationalSum(self, A, B):
        results = []
        temp_arr = []
        A.sort()
        self.combineHelp(A, temp_arr, results, B, 0)
        return results


ob = Solution()
print(ob.combinationalSum([7, 2, 6, 5], 16))
