class Solution:

    def lookandsay(self, n):
        stri = "1"
        if n == 1:
            return "1"
        # generate all string from 1 to n
        for i in range(1, n):
            temp = stri
            prev_value = ""
            count = 0
            stri = ""
            for i in range(len(temp)):
                # for the first time assign prev_value and count
                if i == 0:
                    prev_value = temp[i]
                    count =1
                    continue
                # if current is same as previous then increment count
                if temp[i] == prev_value:
                    count += 1
                # otherwise append the string and reset count as 1
                else:
                    stri += str(count) + prev_value
                    count = 1
                prev_value = temp[i]
            # for the last time append the string to its count and last value
            stri += str(count) + prev_value
        return stri


ob = Solution()
print(ob.lookandsay(20))
