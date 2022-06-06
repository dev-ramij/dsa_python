# There are n trees in a forest. The heights of the trees is stored in array tree[],
# where tree[i] denotes the height of the ith tree in the forest.
# If the ith tree is cut at a height H, then the wood collected is tree[i] - H, provided tree[i] > H.
# If the total woods that needs to be collected is exactly equal to k,
# find the height H at which every tree should be cut (all trees have to be cut at the same height).
# If it is not possible then return -1 else return H.


class Solution:

    def find_height(self, tree, n, k):
        tree.sort()
        if tree[n - 1] == k:
            return k
        low, high = tree[0], tree[n - 1]
        while low <= high:
            mid = (low + high) // 2
            sum = 0
            for i in range(n):
                curr_idx = n - 1 - i
                if tree[curr_idx] > mid:
                    sum += (tree[curr_idx] - mid)
                else:
                    break
            if sum == k:
                return mid
            if sum > k:
                low = mid+1
            else:
                high = mid -1
        return -1


ob = Solution()
print(ob.find_height([2, 3, 5, 2, 4], 5, 6))
