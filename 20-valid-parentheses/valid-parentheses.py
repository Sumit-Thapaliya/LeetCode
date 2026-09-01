class Solution:
    def isValid(self, s):
        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)  #([

            else:
                if not stack:
                    return False

                top = stack.pop() #top=[

                if c == ')' and top != '(':  #c=) and top=( so true 
                    return False

                if c == ']' and top != '[':  #c=] and top=[ so true 
                    return False

                if c == '}' and top != '{':
                    return False

        return not stack