class Solution(object):
    def buildArray(self, target, n):
        arr = []
        j = 0

        for i in range(1, n + 1):

            arr.append("Push")

            if i == target[j]:
                j += 1
            else:
                arr.append("Pop")

            if j == len(target):
                break

        return arr