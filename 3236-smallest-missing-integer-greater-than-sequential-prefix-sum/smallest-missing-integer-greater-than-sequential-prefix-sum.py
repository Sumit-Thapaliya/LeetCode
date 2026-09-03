class Solution(object):
    def missingInteger(self, nums):
        # Find the sum of the longest consecutive prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest number >= total
        # that is not present in nums
        while total in nums:
            total += 1

        return total