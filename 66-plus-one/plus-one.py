class Solution(object):
    def plusOne(self, digits):
        num = int(''.join(map(str, digits)))
        num=num+1

        # num = 0
        # for digit in arr:
        # num = num * 10 + digit

        arr = list(map(int, str(num)))

        # arr = []

        # while num > 0:
        #     digit = num % 10
        #     arr.append(digit)
        #         num = num // 10

        # arr.reverse()
        return arr