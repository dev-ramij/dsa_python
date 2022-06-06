class Solution:

    def isGreater(self, stackTop, expression):
        if expression == "^":
            return True
        elif expression == "*" or expression == "/" and stackTop != "^":
            return True
        elif expression == "+" or expression == "-" and stackTop not in ["*","/","^"]:
            return True
        return False

    def isOp(self, expression):
        return expression in ["+", "-", "*", "/", "^"]

    def InfixtoPostfix(self, exp):
        stack = []
        postfix = ""
        for char in exp:
            if char == "(":
                stack.append(char)
            elif char == ")":
                stackTop = stack[len(stack) - 1]
                while stackTop != "(":
                    postfix += stack.pop()
                    stackTop = stack[len(stack) - 1]
            elif self.isOp(char):
                if len(stack) == 0:
                    stack.append(char)
                else:
                    stackTop = stack[len(stack) - 1]
                    if self.isGreater(stackTop, char):
                        stack.append(char)
                    else:
                        while not self.isGreater(stackTop,
                                                 char) and len(stack) > 0:
                            postfix += stack.pop()
                            stackTop = stack[len(stack) - 1]
                        stack.append(char)
        while len(stack) >0:
            postfix+= stack.pop()
        return postfix
