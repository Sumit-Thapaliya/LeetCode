class Solution(object):
    def findDisappearedNumbers(self, nums):

        n = len(nums)

        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        answer = []

        for i in range(n):
            if nums[i] > 0:
                answer.append(i + 1)

        return answer