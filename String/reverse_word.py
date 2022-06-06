class Solution:

    #Function to reverse words in a given string.
    def reverseWords(self, S):
        str_arr = S.split('.')
        rev_str = ""
        for i in range(len(str_arr), 0, -1):
            rev_str+= str_arr[i-1] 
            if i -1 > 0:
                rev_str += "."

        return rev_str


ob = Solution()
print(ob.reverseWords("i.like.this.program.very.much"))