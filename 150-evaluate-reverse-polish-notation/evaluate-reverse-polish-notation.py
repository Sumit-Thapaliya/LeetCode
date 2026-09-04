class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for x in tokens:
            if x not in ["+", "-", "*", "/"]:
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()

                if x == "+":
                    stack.append(a + b)

                elif x == "-":
                    stack.append(a - b)

                elif x == "*":
                    stack.append(a * b)

                elif x == "/":
                    result = abs(a) // abs(b)

                    if (a < 0) != (b < 0):
                        result = -result

                    stack.append(result)

        return stack[0]