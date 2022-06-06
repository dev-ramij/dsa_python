class Solution:

    def rearrangeString(self, str):
        str_arr = []
        res_arr = []
        for i in range(len(str)):
            str_arr.append(str[i])
            res_arr.append("#")
        str_arr.sort()
        i = 0
        str_idx = 0
        # fill the even position
        while i < len(str):
            if str_idx > 0 and str_arr[str_idx] == res_arr[i-1]:
                return -1
            res_arr[i] = str_arr[str_idx]
            str_idx += 1
            i += 2
        i = 1
        # fill the odd position
        while i < len(str):
            if str_idx > 0 and str_arr[str_idx] == res_arr[i-1]:
                return -1
            res_arr[i] = str_arr[str_idx]
            str_idx += 1
            i += 2
        return "".join(res_arr)


ob = Solution()
print(ob.rearrangeString("kkk"))