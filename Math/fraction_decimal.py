class Solution:

    def fractionToDecimal(self, numerator, denominator):
        if denominator == 0:
            return None
        if numerator == 0:
            return "0"
        sign = 1
        if numerator < 0 ^ denominator < 0:
            sign = -1
        res = ""
        initial = numerator // denominator
        if sign == -1:
            res += "-"
        res += str(initial)
        if numerator % denominator == 0:
            return res
        res += "."
        mp = {}
        rem = numerator % denominator
        index = 0
        repeated = False
        while rem != 0 and not repeated:
            if ( rem in mp):
 
                index = mp[rem]
                repeated = True
                break
            
            else:
                mp[rem] = len(res)
    
            rem = rem * 10
 
        # Calculate quotient, append it to result
        # and calculate next remainder
            temp = rem // denominator
            res += str(temp )
            rem = rem % denominator

        if repeated:
            left_str = res[:index]
            right_str = res[index:]
            res = left_str + "(" + right_str + ")"
        return res


obj = Solution()
print(obj.fractionToDecimal(1, 3))
