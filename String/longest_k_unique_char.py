

class Solution:

    def longestKSubstr(self, s, k):
        hashMap = {}
        l = 0
        count = 0
        maxLength = -1
        # get all unique value assigned their count to 0
        for i in range(len(s)):
            hashMap[s[i]] = 0
        # traverse the string
        for i in range(len(s)):
            # detect the new character and increment the count
            if hashMap[s[i]] == 0:
                count += 1
            hashMap[s[i]] += 1
            # if count == k assigned new max length if found
            if count == k:
                if i - l+1 > maxLength:
                    maxLength = i - l +1
            # if count is greater move the left pointer to right
            while count > k:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    count -= 1
                l += 1
        return maxLength
                


ob = Solution()
print(ob.longestKSubstr("aabacbebebe", 3))
