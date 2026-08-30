class Solution(object):
    def findErrorNums(self, nums):
        duplicate = 0
        missing = 0

        for i in range(len(nums)):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                duplicate = abs(nums[i])
            else:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [duplicate, missing]

a = Solution()

nums = [1, 1]

print(a.findErrorNums(nums))