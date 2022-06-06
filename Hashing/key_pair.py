class Solution:

    def hasArrayTwoCandidates(self, arr, n, x):
        hashmap = {}
        for i in range(n):
            remaining = x - arr[i]
            if remaining in hashmap:
                print(remaining, arr[i], hashmap[remaining])
                return "YES"
            hashmap[arr[i]] = i
        return "NO"


ob = Solution()
print(
    ob.hasArrayTwoCandidates([
        335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492,
        996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896,
        448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334
    ], 42, 468))
