# Alogirthm:
# Height can be 0 to Max(tree). we can cut from 0 to max of the forest.
# We need to find in which height we will get the proper wood(k).
# for that we can use binary search to find it

class Solution:

    def find_height(self, tree, n, k):
        if k == 0:
            return -1
        tree.sort(reverse=True)
        low = 0
        high = tree[0]
        # searching in which height will get the k 
        while low <= high:
            mid = (low + high) // 2
            wood = 0
            # calculating wood which will be collected from the forest
            for i in range(n):
                if tree[i] <= mid:
                    break
                wood += (tree[i] - mid)
            if wood == k:
                return mid
            if wood > k:
                low = mid + 1
            else:
                high = mid - 1
        return -1

ob = Solution()
print(ob.find_height([54, 5, 65, 82, 40, 21, 65], 7, 86))