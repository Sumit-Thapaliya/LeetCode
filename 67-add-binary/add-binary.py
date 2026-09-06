class Solution(object):
    def addBinary(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)
        result=bin(num1 + num2)[2:]
        return result
        