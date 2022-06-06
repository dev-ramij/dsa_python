


class Solution:
    
    def getTheOppositeBracket(self,bracket):
        if bracket == ")":
            return "("
        elif bracket == "}":
            return "{"
        elif bracket == "]":
            return "["

    def isOpenBracket(self,bracket):
        return bracket == "(" or bracket == "{" or bracket == "["
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        stk = []
        if len(x) < 2:
            return False
        for brkt in x:
            if self.isOpenBracket(brkt):
                stk.append(brkt)
            else:
                front_brack = self.getTheOppositeBracket(brkt)
                if len(stk) == 0:
                    return False
                last_el = stk[len(stk)-1]
                if front_brack == last_el:
                    stk.pop()
                else:
                    return False
        if len(stk) == 0:
            return True
        return False

ob = Solution()
print(ob.ispar(']]]'))

