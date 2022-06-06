# There might be 3 condition
# 1. stack is empty in that case append the char and reset count as 1
# 2. if stack top is equal to the char then there may be two condition
# a. if we found k consecutive characters: 
#       then we will pop all consecurive characters
#       but there is one more case may be there is some pre stored consecutive character
#       example: fggeeeg and k = 3 output should be fggg -> f but we lost the count of g
#       so we need to reconsider the g count
# b. we didn't reach to the k then add to stack and increment count
# 3. stack is not empty and char is not same as stack top

class Solution:
    def Reduced_String(self, k, s):
        
        if k ==1:
            return ""
        stk = []
        count = 0
        for char in s:
            # condition 1.
            if len(stk) == 0:
                stk.append(char)
                count = 1
            # condition 2.
            elif stk[len(stk) - 1] == char:
                # reach the k, checking k-1 because haven't count the current
                if count == k-1:
                    # pop all consecutive chars
                    for i in range(k-1):
                        stk.pop()
                    # reset count
                    count = 1
                    # logic to count the prev characteres 
                    i = len(stk) -1
                    if i > 0:
                        prev = stk[i]
                        while i > 0:
                            curr = stk[i-1]
                            if curr == prev:
                                count +=1
                                i-=1
                            else:
                                break
                # condition b.
                else:
                    stk.append(char)
                    count += 1
            # condition 3.
            else:
                stk.append(char)
                count = 1
        return "".join(stk)

ob = Solution()
print(ob.Reduced_String(2,"uxdctqmzkwfgxfccpnrfapkremmvwkzlyimsyzxlvhgncksajsnffnfitrhhvybkcwxjqejxmmempdbdcaxekpjgutxtvklkpqca"))
