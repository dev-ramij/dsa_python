class Solution:

    def isGreater(self, stackTop, value):

        if value == "+" and stackTop == "(":
            return True
        elif value == "-" and stackTop == "(":
            return True
        elif value == "*" and (stackTop == "+" or stackTop == "-"
                               or stackTop == "("):
            return True
        elif value == "/" and (stackTop == "^" or stackTop == "-"
                               or stackTop == "("):
            return True
        elif value == "^" or value == "(":
            return True
        else:
            return False

    def isOp(self, char):
        return char == "+" or char == "-" or char == "*" or char == "/" or char == "^" or char == "("

    def InfixtoPostfix(self, exp):
        postFix = ""
        stack = []
        for char in exp:

            if char == ")":
                lastItem = stack.pop()
                # pop and insert until found (
                while lastItem != "(" and len(stack) > 0:
                    postFix += lastItem
                    lastItem = stack.pop()

                continue

            stackTop = None
            if len(stack) > 0:
                stackTop = stack[len(stack) - 1]
            if self.isOp(char):
                # push if operator is greater than stacktop
                if self.isGreater(stackTop, char) or stackTop is None:
                    stack.append(char)
                else:
                    # pop until found the smaller operator
                    while len(stack) > 0 and not self.isGreater(
                            stackTop, char):
                        postFix += stackTop
                        stack.pop()
                        if len(stack) == 0:
                            break
                        stackTop = stack[len(stack) - 1]
                    # append the operator
                    stack.append(char)
            # append alphabet
            else:
                postFix += char
        for char in stack:
            postFix += char

        return postFix


ob = Solution()
print(ob.InfixtoPostfix("a+b*(c^d-e)^(f+g*h)-i"))
